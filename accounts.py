class  Accounts :
    '''
    This a class that generates new instances of accounts .
    '''
    Account_list = []
    def __init__( self,fullname,usernname,password,phone_number,email) :
        
        '''
        __init__  methods that  help us to create  properties of our obbjects 
         

        Args:
            names: New account  fullname.
            username : New account username
            passwod : New accounnt  password
            p_number: New account phone number.
            email : New  email address.
            
        '''


        self.names = fullname
        self.username = usernname
        self.password = password
        self.phone_number  = phone_number
        self.email =  email
    

    def save_account(self):

        '''
        save_account method saves contact objects into contact_list
        '''

        Accounts.Account_list.append(self)