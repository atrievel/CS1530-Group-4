import os
import binascii

# debug config for CodeFeed 
class DebugConfig(object):
    DEBUG=True
    TESTING=False
    SECRET_KEY=binascii.hexlify(os.urandom(24))
    USERNAME='debug'
    PASSWORD='debug'
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    SQLALCHEMY_DATABASE_URI='sqlite:///codefeed_debug.db'

# default config for CodeFeed 
class ReleaseConfig(object):
    DEBUG=False
    TESTING=False
    SECRET_KEY=binascii.hexlify(os.urandom(24))
    USERNAME='admin'
    PASSWORD='something_really_hard_to_guess_like_this_example_maybe?'
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    SQLALCHEMY_DATABASE_URI='sqlite:///codefeed_release.db'

class TestingConfig(object):
    DEBUG=False
    TESTING=True
    SECRET_KEY=binascii.hexlify(os.urandom(24))
    USERNAME='testing'
    PASSWORD='testing'
    SQLALCHEMY_TRACK_MODIFICATIONS=True
    SQLALCHEMY_DATABASE_URI='sqlite:///codefeed_testing.db'
    #TRAP_HTTP_EXCEPTIONS=True ##only set this to true if testing HTTP status codes
    #TRAP_BAD_REQUEST_ERRORS=True ##only set this to true if testing any request errors