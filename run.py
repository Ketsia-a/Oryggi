from user import User
from credentials import Credentials

def create_users(username,password):
    """
    Function to create a new user
    """
    new_user = User(username,password)
    return new_user


def save_users(user):
    """
    Function to save user
    """
    user.save_user()


def delete_users(user):
    """
    Function to delete a user
    """
    user.delete_user()


def create_credentials(account,username,password):
    """
    Function to create a new credential
    """
    new_credential = Credential(account,username,password)
    return new_credential 

def save_credentials(credential):
    """
    Function to save credential
    """
    redentials.save_credential()

def display_all_credential():
    """
    Function that displays all credentials
    """
    return Credentials.display_all_credential()


def password_generates():
    """
    Function that generates a password for the user
    """
    return Credentials.password_generate()

def delete_credential(credential):
    """
    Function to delete credentials
    """
    credentials.delete_credentials()

def find_credential(name):
    """
    Function that finds in credential a account name and returns the credentials that matches that account name.
    """
    return Credentials.find_by_name(name)

def credential_exists(acccount_username):
    """
    Function that checks if a credential exists and return true or false.
    """
    return Credentials.credential_exist(account_username)

def main():
    tprint("Oryggi")
    print('\n')
    print('\n')
    print('Welcome to')+('Oryggi')+(' your password locker.')
    print('What is your name?')
    username=input()
    print('\n')
    print(f"Hello {username}, complete the following  to create your new account with us")
    print('\n')
    
    print("First Name")
    first_name=input()
    print("Last Name")
    last_name=input()
    print("Enter password")
    password=input()
    
    save_users(create_users(username,password))
    print('\n')
    print(f"Hello {username}, Your account has been created succesfully!")
    print(f"Your password is:{password}")
    print('\n')
   
    print("Enter your User name and your Password to log in:")
    username = input("username: ")
    password = input("password: ")

    if login_users(username,password) == None:
        print('\n')
        print("Please try again")
        print('\n')
       
    else:
        login_users(username,password)
        print('\n')
        print(f"Hello {username}. Welcome To Oryggi")
        print('\n')
        
    while True:
        print("Use these short codes:")
        print('\n')
        print("To create a new credential:    NC\nDisplay Credentials:        DC\nFind a credential:          FC\nDelete credential:          DL\nGenerate a random password: GP\nExit the application:       EX \n")
        short_code = input()
        print('\n')

        if short_code == 'abcd':
            print('New Credential','underlined')
            print('Account name ')
            name=input()
            print('Username ')
            account_username=input()
            print('\n')
            while True:
            print("-Type your own password:   YP\n-Generate random Password: GP")
            password_Choice = input()

            if password_Choice == 'yp':
             account_password = input("Enter Your Own Password\n")
              break
    
            elif password_Choice == 'gp':
             account_password = password_generates()
              break
           
            else:
                    print("Invalid password please try again")
            
        save_credentials(create_credentials(name,account_username,account_password))
            print('\n')
            print(f"Account Credential details:")
             print('\n')
            print(f"Account-name: {name}\nUsername: {account_username}\nPassword:{account_password}")
            print('\n')
            print(f"{acoount_username} what else do you want to do?")
            print('\n')

        elif short_code == "dc":
            print('\n')
            if display_all_credential():
                print("These are your credential accounts: ")
                print('\n')
                for name in display_all_credential():
                    print(f"Account: {name.name} \n Username: {account_username}\n Password: {account_password}")
                    print('\n')
            else:
                print("You don't have any credentials saved yet.....")
                print('\n')        

         elif short_code == "fc":
            print()
            print("Enter the username of the Credential you want to search for")
            search_account_username = input()
            if credential_exists(search_account_name):
                search_credential = find_credential(search_account_username)
                print('\n')
                print(f"Account Name : {search_credential.name}")
                print(f"Username: {search_credential.account_username}")
                print(f"Password :{search_credential.account_password}")
                print('\n')
                print('\n')
            else:
                print("That Credential does not exist")
                print('\n')        
        
        elif short_code == 'dl':
            print('\n')
            print("Enter the username of the Credential you want to delete")
            search_username = input().lower()
            if credential_exists(search_username):
                search_credential = find_credential(search_username)
                print("*"*50)
                search_credential.delete_credentials()
                print(f"{search_credential.username} stored credentials deleted")
                print('*'*50)
            else:
                print("The Credential does not exist anymore in your store")