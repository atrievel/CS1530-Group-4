import config
from flask import Flask, request, redirect, render_template, url_for, flash, jsonify, session, Response, json
from datetime import datetime
from functools import wraps
from flask.ext.bcrypt import Bcrypt
from database import db, User, Category, Thread, Comment, Friendship, CommentVote, ThreadVote, Message
import os