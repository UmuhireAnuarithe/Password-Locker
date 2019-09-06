import unittest
from accounts import Accounts

class TestAccount(unittest.TestCase):

        '''
        Test class that defines test cases for the contact class behaviours.

        Args:
            unittest.TestCase: TestCase class that helps in creating test cases
        '''

        def setUp(self):        
            '''
            Set up method to run before each test cases.
            '''
            self.new_account = Accounts("Ane kofi", "akofi", "12a", "22550", "ak@gmail.com")

        def test_init(self):
            '''
            test_init test case to test if the object is initialized properly
            '''

            self.assertEqual(self.new_account.names,"Ane kofi")
            self.assertEqual(self.new_account.username,"akofi")
            self.assertEqual(self.new_account.password,"12a")
            self.assertEqual(self.new_account.phone_number,"22550")
            self.assertEqual(self.new_account.email,"ak@gmail.com")
        

        def test_save_account(self):
            '''
            test_save_account test case to test if the account object is saved into
            the account list
            '''
            self.new_account.save_account() 
            self.assertEqual(len(Accounts.Account_list),1)

        def test_login_account(self) :
            '''
            test_login_account test case test if the username and password logged in are correct .
            '''

            self.assertEqual(self.new_account.username,"")
            self.assertEqual(self.new_account.password,"")
        
if __name__ == '__main__':
    unittest.main()