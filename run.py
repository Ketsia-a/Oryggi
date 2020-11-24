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
