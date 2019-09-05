import unittest
from accounts import Accounts

class TestContact(unittest.TestCase):

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
    

    

if __name__ == '__main__':
    unittest.main()
