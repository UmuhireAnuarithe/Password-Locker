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

def display_accounts():
    '''
    Function that returns all the saved accounts
    '''
    Accounts.display_accounts()


def find_account(number):
        '''
        Function that finds a account by username and password then returns the account .
        '''
        return Accounts.login_by_user("username", "password")


def main():
        print("Hello Welcome to password locker. What is your name?")
        user_name = input()
        print(f"Hello {user_name}. what would you like to do?")
        print('\n')

while True:
            print("Use these short codes : ca - create a new account, da - dispay account ,dc - display credentials,li - login, ex -exit your accounnt ")

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
                save_accounts(create_account(fullname, username,
                                            password, phone_number, email))
                print('\n')
                print(f"New Account {fullname} created")
                print('\n')

            elif short_code == 'li':

                print("Enter your Username")

                search_username = input()
                print("Enter your password")
                search_password = input()
                if check_existing_accounts(search_username) and ckeck_existing_accounts(search_password):
                    search_username == find_account(search_username) and search_password == find_account(search_password)
                    print(f"{search_account.username} SUccessfully logrd in ")
                    print(f"")

                        # print(f"Phone number.......{search_contact.phone_number}")
                        # print(f"Email address.......{search_contact.email}")
                else:
                        print("That account does not exist")


            elif short_code == 'da':

                if display_accounts():
                    print("Here is a list of all your account created")
                    print('\n')

                    for account in display_accounts():
                        print(f"{account.fullname} {account.username} .....{account.phone_number}{account.password} {account.email}")

                        print('\n')
                else:
                    print('\n')
                    print("You don't have any account created yet")


if __name__ == '__main__':

    main()
