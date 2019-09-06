class  Accounts :
    '''
    This a class that generates new instances of accounts .
    '''
    Account_list = []
    def __init__( self,fullname,username,password,phone_number,email) :
        
        '''
        __init__  methods that  help us to create  properties of our obbjects 
         

        Args:
            names: New account  fullname.
            username : New account username
            passwod : New accounnt  password
            p_number: New account phone number.
            email : New  email address.
            
        '''


        self.fullname = fullname
        self.username = username
        self.password = password
        self.phone_number  = phone_number
        self.email =  email
    

    def save_account(self):

        '''
        save_account method saves contact objects into contact_list
        '''

        Accounts.Account_list.append(self)

    @classmethod
    def display_account(cls):
        '''
        method that returns the account list
        '''
        return cls.Account_list
    

    @classmethod
    def login_by_user(cls,username,password):
        '''
        Method that takes in a username and password to returns the account that matches that number.

        Args:
            number: password and username to search for
        Returns :
            Account  of person that matches the username and password.
        '''

        for account in cls.Account_list:
            if account.username == username and account.password == password :
                return account


    @classmethod
    def account_exist(cls,username,password):
        '''
        Method that checks if a account exists from the account list.
        Args:
            number: Phone number to search if it exists
        Returns :
            Boolean: True or false depending if the contact exists
        '''
        for account in cls.Account_list:
             if account.username == username and account.password == password :
                return account


        return True