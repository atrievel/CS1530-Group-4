import os
import binascii

# debug config for CodeFeed 
class DebugConfig(object):
    DEBUG=True,
    SECRET_KEY=binascii.hexlify(os.urandom(24)),
    USERNAME='debug',
    PASSWORD='debug',
    SQLALCHEMY_TRACK_MODIFICATIONS=False,
    SQLALCHEMY_DATABASE_URI='sqlite:///codefeed_debug.db'

# default config for CodeFeed 
class ReleaseConfig(object):
    DEBUG=False,
    SECRET_KEY=binascii.hexlify(os.urandom(24)),
    USERNAME='admin',
    PASSWORD='something_really_hard_to_guess_like_this_example_maybe?',
    SQLALCHEMY_TRACK_MODIFICATIONS=False,
    SQLALCHEMY_DATABASE_URI='sqlite:///codefeed_release.db'