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