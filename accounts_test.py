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
        self.new_account = Accounts(
            "Ane kofi", "akofi", "12a", "22550", "ak@gmail.com")

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_account.fullname, "Ane kofi")
        self.assertEqual(self.new_account.username, "akofi")
        self.assertEqual(self.new_account.password, "12a")
        self.assertEqual(self.new_account.phone_number, "22550")
        self.assertEqual(self.new_account.email, "ak@gmail.com")

    def test_save_account(self):
        '''
        test_save_account test case to test if the account object is saved into
        the account list
        '''
        self.new_account.save_account()
        self.assertEqual(len(Accounts.Account_list), 3)

    def test_login_by_user(self):
        '''
        test to check if we can find a contact by phone number and display information
        '''

        self.new_account.save_account()
        test_account = Accounts("Umuhire", "Anuarithe", "222","0785460271","a@gmail.com") 
        test_account.save_account()
        found_account = Accounts.login_by_user("Anuarithe", "222")
        
        self.assertEqual(found_account.username, test_account.username)
        self.assertEqual(found_account.fullname, test_account.fullname)
        self.assertEqual(found_account.password, test_account.password)
        self.assertEqual(found_account.phone_number, test_account.phone_number)
        self.assertEqual(found_account.email, test_account.email)


if __name__ == '__main__':
    unittest.main()
