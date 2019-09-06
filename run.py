#!/usr/bin/env python3.6
from accounts import Accounts
from credentials import Credentials


def create_account(fullname, username, password, phone_number, email):
        '''
        Function to create a new account
        '''
        new_account = Accounts("Ane kofi", "akofi", "12a", "22550", "ak@gmail.com")
        return new_account

def save_accounts(account):
        '''
        Function to save accounnt
        '''
        account.save_account()


def login_account(number):
        '''
        Function that finds a account by username and password then returns the account .
        '''
        return Accounts.login_by_user("username", "password")


def create_credentials(appName,username,password):
    '''
    Function to create a new contact
    '''
    new_credential = Credentials(f"twitter", "akofi", "12a")
    return new_credential

def store_credentials(self):

        '''
        store_credential method saves contact objects into credential list
        '''

        Credentials.Credentials_list.append(self)

def display_credentials(cls):
        '''
        method that returns the credential list
        '''
        return cls.Credentials_list

 
     

def main():
        print("Hello Welcome to password locker. What is your name?")
        user_name = input()
        print(f"Hello {user_name}. what would you like to do?")
        print('\n')

while True:
            print("Use these short codes : ca - create a new account, 44 - create credential ,dc - display credentials,log- login, ex -exit your accounnt ")

            short_code = input().lower()

            if short_code == 'ca':

                print("New account")
                print("*"*10)

                print("Full name ....")
                fullname = input()

                print("User name ....")
                username = input()

                print(" Password ....")
                password = input()

                print("Phone number ...")
                phone_number = input()

                print("Email address ...")
                email = input()

                # create and save new account.
                save_accounts(create_account(fullname, username, password, phone_number, email))
                print('\n')
                print(f"New Account {fullname} successfully created")
                print('\n')

 ###########*********************************************#################### credentials
            if short_code == '44':

                print("New credential")
                print("*"*10)

                print(" App name....")
                appName = input()

                print("User name ....")
                username = input()

                print(" Password ....")
                password = input()

                store_credentials(create_credentials(appName, username, password))
                print('\n')
                print(f"New {appName} credential well created ")

                # print("Your credentials gererated properly")

            elif short_code == 'dc':

                            if display_credentials():
                                    print("Here is a list of all your credentilas")
                                    print('\n')

                                    for credential in display_credentials():
                                            print(f"{credential.appName} {credential.username} {credential.password}")

                                    print('\n')
                            else:
                                    print('\n')
                                    print("You dont seem to have any account saved yet")
                                    print('\n')


if __name__ == '__main__':

    main()
