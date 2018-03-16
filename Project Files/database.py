from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32))
    password_hash = db.Column(db.String(128))
    name = db.Column(db.String(64))
    email = db.Column(db.String(64))
    biography = db.Column(db.String(256))
    creation_date = db.Column(db.DateTime)
    is_validated = db.Column(db.Boolean, default=False)
    last_login = db.Column(db.DateTime)

    threads = db.relationship('Thread', backref='user', lazy=True)
    comments = db.relationship('Comment', backref='user', lazy=True)
    thread_votes = db.relationship('ThreadVote', backref='user', lazy=True)
    comment_votes = db.relationship('CommentVote', backref='user', lazy=True)

    def __init__(self, username, password_hash, name, email, biography, creation_date, is_validated, last_login):
        self.username = username
        self.password_hash = password_hash
        self.name = name
        self.email = email
        self.biography = biography
        self.creation_date = creation_date
        self.is_validated = is_validated
        self.last_login = last_login

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32))
    description = db.Column(db.String(512))

    def __init__(self, name, description):
        self.name = name
        self.description = description

class Thread(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    title = db.Column(db.String(256))
    body = db.Column(db.String(2048))
    creation_date = db.Column(db.DateTime)

    categories = db.relationship('Category', backref='user', lazy=False)

    def __init__(self, category_id, user_id, title, body, creation_date):
        self.category_id = category_id
        self.user_id = user_id
        self.title = title
        self.body = body
        self.creation_date = creation_date

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    thread_id = db.Column(db.Integer, db.ForeignKey('thread.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    body = db.Column(db.String(1024))
    creation_date = db.Column(db.DateTime)

    def __init__(self, thread_id, user_id, body, creation_date):
        self.thread_id = thread_id
        self.user_id = user_id
        self.body = body
        self.creation_date = creation_date

class Friendship(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user1_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user2_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    creation_date = db.Column(db.DateTime)

    user1 = relationship('User', foreign_keys=[user1_id])
    user2 = relationship('User', foreign_keys=[user2_id])

    def __init__(self, user1_id, user2_id, creation_date):
        self.user1_id = user1_id
        self.user2_id = user2_id
        self.creation_date = creation_date

class ThreadVote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    thread_id = db.Column(db.Integer, db.ForeignKey('thread.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    value = db.Column(db.Boolean)

    def __init__(self, thread_id, user_id, value):
        self.thread_id = thread_id
        self.user_id = user_id
        self.value = value

class CommentVote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    comment_id = db.Column(db.Integer, db.ForeignKey('comment.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    value = db.Column(db.Boolean)

    def __init__(self, comment_id, user_id, value):
        self.comment_id = comment_id
        self.user_id = user_id
        self.value = value

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user1_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user2_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    body = db.Column(db.String(1024))
    creation_date = db.Column(db.DateTime)

    user1 = relationship('User', foreign_keys=[user1_id])
    user2 = relationship('User', foreign_keys=[user2_id])

    def __init__(self, user1_id, user2_id, body, creation_date):
        self.user1_id = user1_id
        self.user2_id = user2_id
        self.body = body
        self.creation_date = creation_date
