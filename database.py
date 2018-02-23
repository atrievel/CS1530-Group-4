from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32))
    password_hash = db.Column(db.String(128))
    name = db.Column(db.String(64))
    email = db.Column(db.String(64))
    biography = db.Column(256)
    creation_date = db.Column(db.DateTime)
    is_validated = db.Column(db.Boolean, default=False)
    last_login = db.Column(db.DateTime)

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32))
    description = db.Column(db.String(512))

class Thread(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    user_id = db.Column(db.Ingeger, db.ForeignKey('user.id'))
    title = db.Column(db.String(256))
    body = db.Column(db.String(2048))
    creation_date = db.Column(db.DateTime)

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    thread_id = db.Column(db.Integer, db.ForeignKey('thread.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    body = db.Column(db.String(1024))
    creation_date = db.Column(db.DateTime)

class Friendship(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user1_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user2_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    creation_date = db.Column(db.DateTime)

class ThreadVote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    thread_id = db.Column(db.Integer, db.ForeignKey('thread.id'))
    value = db.Column(db.Boolean)

class CommentVote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    comment_id = db.Column(db.Integer, db.ForeignKey('comment.id'))
    value = db.Column(db.Boolean)

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user1_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user2_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    body = db.Column(db.String(1024))
    creation_date = db.Column(db.DateTime)
