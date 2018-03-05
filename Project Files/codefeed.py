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

@app.cli.command('initdb')
def initdb_command():
    """Creates the database tables."""
    db.drop_all()
    db.create_all()
    print('Initialized the database.')

# begin route initialization
@app.route("/", methods=['GET','POST'])
def home():
    return "Welcome to CodeFeed"

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
                flash('Credentials not verified. Please try again or register for a new account')
        else:
            flash('Credentials not verified. Please try again or register for a new account')

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
        try:
            # assert all inputs are valid
            assert User.query.filter_by(username=username).first() == None
            assert password == verify_password
            assert len(password) >= 8
            # assert the email is a valid type
            assert email.utils.parseaddr(email) != ('', '')
        except:
            # if any asserts fall flash an errer message
            flash('Please check the entered information and try submitting again')
            return
        # otherwise add them as a new user
        
        # generate the hash for the password
        pw_hash = bcrypt.generate_password_hash(password)
        new_user = User(username, pw_hash, name, email, current_date)
        new_user.creation_date = datetime.now()
        new_user.is_validated = True
        db.session.add(new_user)
        db.session.commit()
        return render_template('login.html')
        
@app.route("/profile", methods=['GET','POST'])
def myProfile():
    user_id = request.args['user_id']
    if user_id is None:
        return "myProfile"
    elif user_id == "":
        return "myProfile"
    else:
        return "Profile_ID : " + user_id

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
    cat_id = request.args['cat_id']
    if cat_id is None:
        return "Which category?"
    elif cat_id == "":
        return "Which category?"
    else:
        return "Get Category by cat_id : " + cat_id

@app.route("/category/post", methods=['GET','POST'])
def addPost():
    post_id = request.args['post_id']
    if post_id is None:
        return "Which post?"
    elif post_id == "":
        return "Which post?"
    else:
        return "Add post with post_id : " + post_id

@app.route("/category/post/add_comment", methods=['GET','POST'])
@login_required
def addComment():
    post_id = request.args['post_id']
    if post_id is None:
        return "Which post?"
    elif post_id == "":
        return "Which post?"
    else:
        return "Add comment to post_id : " + post_id

if __name__ == '__main__':
    app.run()