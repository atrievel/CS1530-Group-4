from imports import *

# create the application and associated objects
app = Flask(__name__)
bcrypt = Bcrypt(app)

# load default config and override config from an external class
app.config.from_object('config.DebugConfig')

# initialize the database
db.init_app(app)

# login required decorator
# Use @login_required
# before any route to require the user be logged in
# and redirect them to the login page.
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session['user_id'] is None:
            return redirect(url_for('login', next=request.url))
        return f(*args, **kwargs)
    return decorated_function

# Returns the tally of upvotes and downvotes on the given thread    
def get_thread_votes(id):
    votes = ThreadVote.query.filter_by(thread_id=id).all()
    count = 0
    for vote in votes:
        if vote.value:
            count+=1
        else:
            count-=1
    return count

# Returns the tally of upvotes and downvotes on the given comment     
def get_comment_votes(id):
    votes = CommentVote.query.filter_by(comment_id=id).all()
    count = 0
    for vote in votes:
        if vote.value:
            count+=1
        else:
            count-=1
    return count
    
# Returns true if the two ids are freinds    
def are_friends(id1, id2):
    return (Friendship.query.filter_by(user1_id = id1, user2_id = id2).first() is not None or
    Friendship.query.filter_by(user1_id = id2, user2_id = id1).first())

@app.cli.command('initdb')
def initdb_command():
    """Creates the database tables."""
    db.drop_all()
    db.create_all()
    print('Initialized the database.')

# begin route initialization
@app.route("/", methods=['GET'])
def index():
    num_users = db.session.query(User).count()
    num_posts = db.session.query(Thread).count()
    num_groups = db.session.query(Category).count()
    num_up_votes = db.session.query(ThreadVote).filter(ThreadVote.value == True).count() + db.session.query(ThreadVote).filter(CommentVote.value == True).count()
    
    return render_template('landing.html', num_users=num_users, num_posts=num_posts,num_groups=num_groups,num_up_votes=num_up_votes)

@app.route("/login", methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        # Get the user based on the entered username
        user = User.query.filter_by(username=request.form['username']).first()

        if user: 
            pw_hash = user.password_hash #get the password hash from the db

            if bcrypt.check_password_hash(pw_hash, request.form['password']):    
                session['user_id'] = user.id #set the session varaible for the user
                user.last_login = datetime.now()
                db.session.commit() 
                return redirect(url_for('profile'))
            else:
                flash('Credentials not verified. Please try again or register for a new account','error')
                return render_template('login.html')
        else:
            flash('Credentials not verified. Please try again or register for a new account','error')
            return render_template('login.html')
    else:
        return render_template('login.html')
        
@app.route("/logout", methods=['GET'])
@login_required
def logout():
    session.clear()
    return redirect(url_for('login'))
        
@app.route("/register", methods=['GET','POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    elif request.method == 'POST':
        # get all the inputs from the form
        username = request.form['username']
        password = request.form['password']
        verify_password = request.form['verify_password']
        name = request.form['name']
        email = request.form['email']
        current_date = datetime.now()

        try:
            assert User.query.filter_by(username=username).first() is None
        except:
            flash('That username is already taken','error')
            return render_template('register.html')

        try:
            assert password == verify_password
            assert len(password) >= 8
        except:
            flash('The passwords do not match and/or are less than 8 characters long','error')
            return render_template('register.html')

        #otherwise add them as a new user
        # generate the hash for the password
        pw_hash = bcrypt.generate_password_hash(password)
        new_user = User(username, pw_hash, name, email, "", current_date, True, current_date)
      
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))
    else:
        return render_template('register.html')
        
@app.route("/profile", methods=['GET','POST'])
@login_required
def profile():
    user = User.query.filter_by(id=session['user_id']).first()

    if request.method == 'GET':
            return render_template('profile.html', id=user.id, username=user.username,
                                                   name=user.name, email=user.email,
                                                   biography=user.biography,
                                                   creation_date=user.creation_date.strftime("%m/%d/%Y"),
                                                   last_login=user.last_login.strftime("%m/%d/%Y"))
    elif request.method == 'POST':
        updated_profile = request.get_json(force=True)

        try:
            name = updated_profile['name']
            password = updated_profile['password']
            verify_password = updated_profile['verify_password']
            biography = updated_profile['biography']
        except (KeyError, TypeError, ValueError):
            return Response("{'error': 'invalid JSON'}", status=403, mimetype='application/json')

        try:
            assert password == verify_password or (password is None and verify_password is None)
        except:
            return Response("{'updated': false}", status=403, mimetype='application/json')

        user.name = name
        user.email = email
        user.biography = biography
        if password is not None:
            pw_hash = bcrypt.generate_password_hash(password)
            user.password_hash = pw_hash

        db.session.update(user)
        db.session.commit()
        return Response("{'updated': true}", status=200, mimetype='application/json')
    else:
        return render_template('profile.html')

@app.route("/profile/<int:user_id>", methods=['GET'])
def get_profile(user_id):
    user = User.query.filter_by(id=user_id).first()
    return render_template('profile.html', id=user.id, username=user.username,
                                           name=user.name, email=user.email,
                                           biography=user.biography,
                                           creation_date=user.creation_date.strftime("%m/%d/%Y"),
                                           last_login=user.last_login.strftime("%m/%d/%Y"))

@app.route("/profile/messages", methods=['GET','POST'])
@login_required
def getMessages():
    user = User.query.filter_by(id=session['user_id']).first()

    if request.method == 'GET':
        messages = Message.query.filter_by(user2_id=user.id).all()
        messages_parsed = []
        
        # Create a list of tuples containg each messages sender, body, and creation_date
        for message in messages:
            messages_parsed.append((message.username, message.body, message.creation_date))
        
        return render_template('messages.html', messages=messages_parsed)
    elif request.method == 'POST':     
        # Parse the JSON string
        new_message = request.get_json(force=True)
        description = string(new_message['description'])  
        recipient = User.query.filter_by(name=new_message['name']).first()
        
        try:
            assert are_friends(user.id, recipient.id)
        except:
            return Response("{'error': 'users not friends'", status=403, mimetype='application/json')
        
        return Response("{'error': 'none'", status=200, mimetype='application/json')
    else:
        return render_template('messages.html', messages=None)

@app.route("/profile/friends", methods=['GET','POST'])
@login_required
def listFriends():
    user = User.query.filter_by(id=session['user_id']).first()

    if request.method == 'GET':
        # Get a list of all messages sent to the current user
        friends = Frienship.query.filter_by(user1_id=user.id).all()
        friends_parsed = []
        friends.append(Frienship.query.filter_by(user2_id=user.id).all())
        
        # Create a list of tuples containg each messages sender, body, and creation_date
        for friend in friends:
            friends_parsed.append((friend.id, friend.username))
        
        return render_template('friends.html', friends=friends_parsed) 
    elif request.method == 'POST':        
        # Parse the JSON string
        data = request.get_json(force=True)
        user2_id = int(data['user2_id'])
        
        try:
            assert not are_friends(user.id, user2.id)
        except:
            return Response("{'error': 'no friends'", status=403, mimetype='application/json')
        
        return Response("{'error': 'none'", status=200, mimetype='application/json')
    else:
        return render_template('friends.html', friends=None) 

   #TO DO     

@app.route("/categories", methods=['GET'])
def categories():
    if request.method == 'GET':
        # Get a list of all categories
        cats = Category.query.all()
        categories = []

        # Create a list of tuples containg each threads id, name, and description
        for cat in cats:
            categories.append((cat.id, cat.name, cat.description))

        return render_template('categories.html', categories=categories)
    else:
        return render_template('categories.html', categories=None)
        
@app.route("/category", methods=['POST'])
@login_required
def create_category():
    if request.method == 'POST':
        data = request.get_json(force=True)
        name = data['name']
        description = data['description']

        try:
            assert Category.query.filter_by(name=name).first() is None
        except:
            return Response("{'error': 'category exists'}", status=403, mimetype='application/json')

        new_category = Category(name, description)
        db.session.add(new_category)
        db.session.commit()

        return Response("{'error': 'none'}", status=200, mimetype='application/json')

@app.route("/category/", methods=['GET'])
def category():
    if request.method == 'GET':
        category_id = request.args.get('category_id')

        category = Category.query.filter_by(id=category_id).first()
        posts = []

        # Get a list of all threads in the category
        threads = Thread.query.filter_by(category_id=category_id).all()
        
        # Create a list of tuples containg each threads id, title, body, and vote count.
        for thread in threads:
            posts.append((thread.id, thread.title, thread.body, get_thread_votes(thread.id)))
        
        return render_template('category.html', posts=posts, category_name=category.name)
    else:
        return url_for('listCategories')

@app.route("/category/post/", methods=['GET'])
def post():
    if request.method == 'GET':
        post_id = request.args.get('post_id')
        thread = Thread.query.filter_by(id=post_id).first()
        comments = []
        # Get a list of all comments in the thread
        comms = Comment.query.filter_by(thread_id=post_id).all()
        
        # Create a list of tuples containg each comment's id, user, body, creation_date and vote count.
        for comment in comms:
            commenter = User.query.filter_by(id=comment.user_id).first()
            comments.append((comment.id, comment.body, commenter.name, get_comment_votes(comment.id), comment.creation_date.strftime("%m/%d/%Y")))
        
        return render_template('post.html',comments=comments, post_name=thread.title, vote_count = get_thread_votes(thread.id))
    else:
        return url_for('listCategories')
    
@app.route("/category/post", methods=["POST"])
@login_required
def create_post():
    if request.method == 'POST':
        # Parse the JSON string
        data = request.get_json(force=True)

        # Add the post to the database
        new_post = Thread(data['category_id'], session['user_id'], data['title'], data['body'], datetime.now())
        db.session.add(new_post)
        db.session.commit()

        # Check if the post was inserted
        if new_post.id:
            return Response("{'error': 'none'}", status=200, mimetype='application/json')
        else:
            return Response("{'error': 'insert error'}", status=403, mimetype='application/json')
            
@app.route("/category/post/add_comment", methods=['POST'])
@login_required
def create_comment():
    if request.method == 'POST':
        # Parse the JSON string
        data = request.get_json(force=True)

        # Add the comment to database
        new_comment = Comment(data['post_id'], session['user_id'], data['body'], datetime.now())
        db.session.add(new_comment)
        db.session.commit()
        
        # Check if the comment was inserted
        if new_comment.id:
            return Response("{'error': 'none'}", status=200, mimetype='application/json')
        else:
            return Response("{'error': 'insert error'}", status=403, mimetype='application/json')

@app.route('/category/post/vote', methods=['POST'])
@login_required
def addPostVote():
    if request.method == 'POST':
        # Parse the JSON string
        data = request.get_json(force=True)
  
        # Add the vote to the database
        new_vote = ThreadVote(data['post_id'], session['user_id'], data['vote']==1)
        db.session.add(new_vote)
        db.session.commit()

        return Response("{'error': 'none'}", status=200, mimetype='application/json')
        
@app.route('/category/post/comment/vote', methods=['POST'])
@login_required
def addCommentVote():
    if request.method == 'POST':
        #Parse the JSON string
        data = request.get_json(force=True)
        
        #Add the vote to the database
        new_vote = CommentVote(data['comment_id'], session['user_id'], data['vote']==1)
        db.session.add(new_vote)
        db.session.commit()

        return Response("{'error': 'none'}", status=200, mimetype='application/json')

if __name__ == '__main__':
    app.run(debug=True)