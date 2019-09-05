class  Accounts :
    '''
    This a class that generates new instances of accounts .
    '''
    Accounts_list = []
    def __init__( self,names,usernname,password,phone_number,email) :
        
        '''
        __init__  methods that  help us to create  properties of our obbjects 
         

        Args:
            names: New account  fullname.
            username : New account username
            passwod : New accounnt  password
            p_number: New account phone number.
            email : New  email address.
            
        '''


        self.names = names
        self.username = usernname
        self.password = password
        self.phone_number  = phone_number
        self.email =  email
