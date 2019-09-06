import unittest
from credentials import Credentials

class TestCredentials(unittest.TestCase):

    '''
    Test class that defines test cases for the contact class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''

    def setUp(self):        
        '''
        Set up method to run before each test cases.
        '''
        self.new_credential = Credentials("twitter", "akofi", "12a")

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_credential.appName,"twitter")
        self.assertEqual(self.new_credential.username,"akofi")
        self.assertEqual(self.new_credential.password,"12a")

    
    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            # Credentials_list = []


    def test_store_credentials(self):
        '''
        test_store_credential test case to test if the credential object is saved into
         the credential list
        '''
        self.new_credential.store_credentials() 
        self.assertEqual(len(Credentials.Credentials_list),2)

 
    def test_store_multiple_credential(self):
            '''
            test_store_multiple_contact to check if we can save multiple credential
            objects to our credential_list
            '''
            self.new_credential.store_credentials()
            test_credential = Credentials("Twitter","andrew","123") 
            test_credential.store_credentials()
            self.assertEqual(len(Credentials.Credentials_list),4)


    def test_delete_credentials(self):
            '''
            test_delete_credentialsto test if we can remove a credentialst from our credentials list
            '''
            self.new_credential.store_credentials()
            test_credential = Credentials("Twitter","andrew","123")
            test_credential.store_credentials()

            self.new_credential.delete_credential()
            self.assertEqual(len(Credentials.Credentials_list),1)
   


        
    def test_display_all_credential(self):
           '''
           method that returns a list of all credential saved
           '''

           self.assertEqual(Credentials.display_credentials(),Credentials.Credentials_list)


if __name__ == '__main__':
    unittest.main()
