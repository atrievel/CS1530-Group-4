import config
from flask import Flask, request, redirect, render_template, url_for
from datetime import datetime
from flask.ext.bcrypt import Bcrypt
from database import db, User, Category, Thread, Comment, Friendship, CommentVote, ThreadVote, Message