from imports import *

# create the application and associated objects
app = Flask(__name__)
crypto = Bcrypt(app)

# load default config and override config from an external class
app.config.from_object('config.DebugConfig')

# initialize the database 
db.init_app(app)

@app.cli.command('initdb')
def initdb_command():
    """Creates the database tables."""
    db.drop_all()
    db.create_all()
    print('Initialized the database.')

# begin route initialization
@app.route("/")
def home():
	return "Welcome to CodeFeed"

@app.route("/login")
def login():
	return "Login"

@app.route("/logout")
def logout():
	return "Logout"

@app.route("/register")
def register():
	return "Register"

@app.route("/profile")
def myProfile():
	user_id = request.args['user_id']
	if user_id is None:
		return "myProfile"
	elif user_id == "":
		return "myProfile"
	else:
		return "Profile_ID : " + user_id

@app.route("/profile/send_message")
def sendMessage():
	user_id = request.args['user_id']
	if user_id is None:
		return "Send to who?"
	elif user_id == "":
		return "Send to who?"
	else:
		return "Send message to Profile_ID : " + user_id
    
@app.route("/profile/messages")
def getMessages():
	return "getMessages"

@app.route("/profile/friends")
def listFriends():
	return "listFriends"

@app.route("/categories")
def listCategories():
	return "listCategories"

@app.route("/category")
def getCategory():
	cat_id = request.args['cat_id']
	if cat_id is None:
		return "Which category?"
	elif cat_id == "":
		return "Which category?"
	else:
		return "Get Category by cat_id : " + cat_id

@app.route("/category/post")
def addPost():
	post_id = request.args['post_id']
	if post_id is None:
		return "Which post?"
	elif post_id == "":
		return "Which post?"
	else:
		return "Add post with post_id : " + post_id

@app.route("/category/post/add_comment")
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