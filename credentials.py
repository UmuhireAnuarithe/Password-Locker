class  Credentials :
    '''
    This a class that generates new instances of accounts .
    '''
    Credentials_list = []
    def __init__( self,appName,usernname,password) :
        
        '''
        __init__  methods that  help us to create  properties of our objects 
         

        Args:
            appName : new Credentials application
            username : New Credentials username
            passwod : New Credentialst  password
            
            
        '''
        self.appName = appName
        self.username = usernname
        self.password = password
       
    def store_credential(self):

        '''
        store_credential method saves contact objects into credential list
        '''

        Credentials.Credentials_list.append(self) 
     

    def delete_credential(self):

        '''
        delete_credenntial method deletes a saved credential from the credential_list
        '''

        Credentials.Credentials_list.remove(self)