#!/usr/bin/env python3.6
from accounts import Accounts
# from credentials import Credentials


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


def main():
    print("Hello Welcome to password locker. What is your name?")
    user_name = input()
    print(f"Hello {user_name}. what would you like to do?")
    print('\n')


    while True:
        print("Use these short codes : ca - create a new account, dc - display credentials,li - login, ex -exit your accounnt ")

        short_code = input().lower()

        if short_code == 'ca':
            print("New account")
            print("*"*10)

            print("Full name ....")
            fullname= input()

            print("User name ....")
            username = input()
            
            print(" Password ....")
            password  =input()

            print("Phone number ...")
            phone_number = input()

            print("Email address ...")
            email = input()

            # create and save new account.
            save_accounts(create_account(fullname, username, password, phone_number, email))
            print('\n')
            print(f"New Account {fullname} created")
            print('\n')

if __name__ == '__main__':

    main()