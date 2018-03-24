import unittest
import config

class TestDebugMode(unittest.TestCase):
    def setUp(self):
        self.stub = config.DebugConfig

    def test_debug(self):
        self.assertTrue(self.stub.DEBUG)
        
    def test_testing(self):
        self.assertFalse(self.stub.TESTING)    

    def test_secret_key(self):
        self.assertEqual(len(self.stub.SECRET_KEY), 48)
        
    def test_username(self):
        self.assertEqual(self.stub.USERNAME, 'debug')    

    def test_password(self):
        self.assertEqual(self.stub.PASSWORD, 'debug')  
    
    def test_track_modifications(self):
        self.assertFalse(self.stub.SQLALCHEMY_TRACK_MODIFICATIONS)  
    
    def test_database_uri(self):
        self.assertEqual(self.stub.SQLALCHEMY_DATABASE_URI, 'sqlite:///codefeed_debug.db')  

class TestReleaseMode(unittest.TestCase):
    def setUp(self):
        self.stub = config.ReleaseConfig

    def test_debug(self):
        self.assertFalse(self.stub.DEBUG)
        
    def test_testing(self):
        self.assertFalse(self.stub.TESTING)    

    def test_secret_key(self):
        self.assertEqual(len(self.stub.SECRET_KEY), 48)
        
    def test_username(self):
        self.assertEqual(self.stub.USERNAME, 'admin')    

    def test_password(self):
        self.assertEqual(self.stub.PASSWORD, 'something_really_hard_to_guess_like_this_example_maybe?')  
    
    def test_track_modifications(self):
        self.assertFalse(self.stub.SQLALCHEMY_TRACK_MODIFICATIONS)  
    
    def test_database_uri(self):
        self.assertEqual(self.stub.SQLALCHEMY_DATABASE_URI, 'sqlite:///codefeed_release.db')  

class TestTestingMode(unittest.TestCase):
    def setUp(self):
        self.stub = config.TestingConfig

    def test_debug(self):
        self.assertFalse(self.stub.DEBUG)
        
    def test_testing(self):
        self.assertTrue(self.stub.TESTING)    

    def test_secret_key(self):
        self.assertEqual(len(self.stub.SECRET_KEY), 48)
        
    def test_username(self):
        self.assertEqual(self.stub.USERNAME, 'testing')    

    def test_password(self):
        self.assertEqual(self.stub.PASSWORD, 'testing')  
    
    def test_track_modifications(self):
        self.assertTrue(self.stub.SQLALCHEMY_TRACK_MODIFICATIONS)  
    
    def test_database_uri(self):
        self.assertEqual(self.stub.SQLALCHEMY_DATABASE_URI, 'sqlite:///codefeed_testing.db')  


def suite():
    suite = unittest.TestSuite()

    #Tests for Debug configuration
    suite.addTest(TestDebugMode('test_debug'))
    suite.addTest(TestDebugMode('test_testing'))
    suite.addTest(TestDebugMode('test_secret_key'))
    suite.addTest(TestDebugMode('test_username'))
    suite.addTest(TestDebugMode('test_password'))
    suite.addTest(TestDebugMode('test_track_modifications'))
    suite.addTest(TestDebugMode('test_database_uri'))

    #Tests for Release configuration
    suite.addTest(TestReleaseMode('test_debug'))
    suite.addTest(TestReleaseMode('test_testing'))
    suite.addTest(TestReleaseMode('test_secret_key'))
    suite.addTest(TestReleaseMode('test_username'))
    suite.addTest(TestReleaseMode('test_password'))
    suite.addTest(TestReleaseMode('test_track_modifications'))
    suite.addTest(TestReleaseMode('test_database_uri'))

    #Tests for Testing configuration
    suite.addTest(TestTestingMode('test_debug'))
    suite.addTest(TestTestingMode('test_testing'))
    suite.addTest(TestTestingMode('test_secret_key'))
    suite.addTest(TestTestingMode('test_username'))
    suite.addTest(TestTestingMode('test_password'))
    suite.addTest(TestTestingMode('test_track_modifications'))
    suite.addTest(TestTestingMode('test_database_uri'))
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())