from imports import *

# create the application and associated objects
app = Flask(__name__)
crypto = Bcrypt(app)

# load default config and override config from an external class
app.config.from_object('config.DebugConfig')

# initialize the database 
db.init_app(app)



# login required decorator
# Use
# @login_required
# before any route to require the user be logged in
# and redirect them to the login page.
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if sesssion['user_id'] is None:
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
    votes = CommentVote.query.filter_by(thread_id=id).all()
    count = 0
    for vote in votes:
        if vote.value:
            count+=1
        else:
            count-=1
    return count


@app.cli.command('initdb')
def initdb_command():
    """Creates the database tables."""
    db.drop_all()
    db.create_all()
    print('Initialized the database.')

# begin route initialization
@app.route("/", methods=['GET','POST'])
def home():
    if request.method == 'GET':
        num_users = db.session.query(User).count()
        num_posts = db.session.query(Thread).count()
        num_groups = db.session.query(Category).count()
        num_up_votes = db.session.query(ThreadVote).filter(ThreadVote.value == True).count()
        + db.session.query(ThreadVote).filter(CommentVote.value == True).count()
        return render_template('landing.html', num_users=num_users, num_posts=num_posts,num_groups=num_groups,num_up_votes=num_up_votes)
@app.route("/login", methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    if request.method == 'POST':
        # Get the user based on the entered username
        user = User.query.filter_by(username=request.form['username']).first()
        if user != None: 
            pw_hash = user.password_hash #get the password hash from the db
            if check_password_hash(pw_hash, requst.form['password']):
                user.last_login = datetime.now()
                db.session.commit()
                session['user_id'] = user.id #set the session varaible for the user
            else:
                flash('Credentials not verified. Please try again or register for a new account','error')
        else:
            flash('Credentials not verified. Please try again or register for a new account','error')

@app.route("/logout", methods=['GET','POST'])
def logout():
    if request.method == 'GET':
        session.clear()
        return render_template('login.html')
        
@app.route("/register", methods=['GET','POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    if request.method == 'POST':
        # get all the inputs from the form
        username = request.form['username']
        password = request.form['password']
        verify_password = request.form['verify_password']
        name = request.form['name']
        email = request.form['email']
        current_date = datetime.now()
        try:
            # assert all inputs are valid
            assert User.query.filter_by(username=username).first() == None
            assert password == verify_password
            assert len(password) >= 8
            # assert the email is a valid type
            assert email.utils.parseaddr(email) != ('', '')
        except:
            # if any asserts fall flash an errer message
            flash('Please check the entered information and try submitting again','error')
            return
        # otherwise add them as a new user
        
        # generate the hash for the password
        pw_hash = bcrypt.generate_password_hash(password)
        new_user = User(username, pw_hash, name, email, current_date, True, current_date)
      
        
        db.session.add(new_user)
        db.session.commit()
        return render_template('login.html')
        
@app.route("/profile", methods=['GET','POST'])
def profile():
    if request.method == 'GET':
        if request.args['user_id'] is None:
            user_id = session['user_id']
        else:
            user_id = request.args['user_id']
        user = User.query.filter_by(id=user_id).first()
        return render_template('profile.hrml', id = user.id,
        username = user.username,
        name = user.name,
        email = user.email,
        biography = user.biography,
        creation_date = creation_date,
        last_login = last_login)
    if request.method == 'POST':
        user = User.query.filter_by(id=session['user_id']).first()
        data = request.get_json(force=True)
        try:
            name = string(data['name'])
            password = string(data['password'])
            verify_password = string(data['verify_password'])
            biography = string(data['biography'])
        except (KeyError, TypeError, ValueError):
            raise JsonError(description='Invalid values.')
        try:
            assert password == verify_password or (password is None and verify_password is None)
            assert email.utils.parseaddr(email) != ('', '')
        except:
            return jsonify(staus=403, updated = False)
        user.name = name
        user.email = email
        user.biography = biography
        if password is not None:
            pw_hash = bcrypt.generate_password_hash(password)
            user.password_hash = pw_hash
        return jsonify(status = 200, updated = True)
@app.route("/profile/send_message", methods=['GET','POST'])
@login_required
def sendMessage():
    user_id = request.args['user_id']
    if user_id is None:
        return "Send to who?"
    elif user_id == "":
        return "Send to who?"
    else:
        return "Send message to Profile_ID : " + user_id
    
@app.route("/profile/messages", methods=['GET','POST'])
@login_required
def getMessages():
    return "getMessages"

@app.route("/profile/friends", methods=['GET','POST'])
@login_required
def listFriends():
    return "listFriends"

@app.route("/categories", methods=['GET','POST'])
def listCategories():
    return "listCategories"

@app.route("/category", methods=['GET','POST'])
def getCategory():
    if request.method == 'GET':
        category_id = request.args['cat_id']
        category = Category.query.filter_by(id=category_id).first()
        posts = []
        # Get a list of all threads in the category
        threads = Threads.query.filter_by(category_id=category_id).all()
        
        # Create a list of tuples containg each threads id, title, body, and vote count.
        for thread in threads:
            post.append((thread.id, thread.title, thread.body, get_thread_votes(thread.id)))
        
        return render_template('category.html',posts=posts, category_name=category.name)
    if request.method == 'POST':
        data = request.get_json(force=True)
        name = string(data['name'])
        description = string(data['description'])
        try:
            assert Category.query.filter_by(name=name).first() is None
        except:
            return jsonify(status = 200)
        new_category = Category(name, description)
        db.session.add(new_category)
        db.sesssion.commit()
        return jsonify(status = 200, id = new_category.id, name= name)
        
@app.route("/category/post", methods=['GET','POST'])
def addPost():
    if request.method == 'GET':
        post_id = request.args['post_id']
        thread = Thread.query.filter_by(id = post_id).first()
        comments = []
        # Get a list of all threads in the category
        comms = Comment.query.filter_by(thread_id=post_id).all()
        
        # Create a list of tuples containg each threads id, title, body, and vote count.
        for comment in comms:
            commenter = User.query.filter_by(id = comment.user_id).first()
            comments.append((comment.id, comment.body, commenter.name, get_comment_votes(comment.id)))
        
        return render_template('post.html',comments=comments, post_name=thread.title, vote_count = get_thread_votes(thread.id))
    
    if request.method == 'POST':
    
        # Check if the user is logged in
        if session['user_id'] is None:
            return jsonify(status = 403)
        
        user = User.query.filter_by(id=session['user_id']).first()
        
        # Parse the JSON string
        data = request.get_json(force=True)
        title = string(data['title'])
        body = string(data['body'])
        cat_id = int(data['category_id'])
        
        # Add the post to the database
        current_date = datetime.now();
        new_post = Thread(cat_id, user.id, title, body, creation_date)
        db.session.add(new_post)
        db.session.commit()
        
        # Check if the post was inserted
        if new_post.id is not None:
            return jsonify(status = 200)
        else:
            return jsonify(status = 403)
            
@app.route("/category/post/add_comment", methods=['GET','POST'])
@login_required
def addComment():
    if request.method == 'POST':
        user = User.query.filter_by(id=session['user_id']).first()
        
        # Parse the JSON string
        data = request.get_json(force=True)
        body = string(data['body'])
        post_id = int(data['post_id'])
        
        current_date = datetime.now();
        # Add the comment to database
        new_comment = Comment(post_id, user.id, body, current_date)
        db.session.add(new_comment)
        db.session.commit()
        
        # Check if the comment was inserted
        if new_comment.id is not None:
            return jsonify(status = 200)
        else:
            return jsonify(status = 403)

@app.route('/category/post/vote', methods=['GET','POST'])
@login_required
def addPostVote():
    if request.method == 'POST':
        user = User.query.filter_by(id=session['user_id']).first()
        
        # Parse the JSON string
        data = request.get_json(force=True)
        post_id = int(data['post_id'])
        vote = int(data['vote']) == 1
        
        # Add the vote to the database
        new_vote = ThreadVote(post_id, use.id, vote)
        db.session.add(new_vote)
        db.session.commit()
        return jsonify(status = 200)
        
@app.route('/category/post/comment/vote', methods=['GET','POST'])
@login_required
def addCommentVote():
    if request.method == 'POST':
        user = User.query.filter_by(id=session['user_id']).first()
        
        # Parse the JSON string
        data = request.get_json(force=True)
        post_id = int(data['post_id'])
        comment_id = int(data['comment_id'])
        vote = int(data['vote']) == 1
        
        # Add the vote to the database
        new_vote = CommentVote(comment_id, user.id, vote)
        db.session.add(new_vote)
        db.session.commit()
        return jsonify(status = 200)
        
if __name__ == '__main__':
    app.run()