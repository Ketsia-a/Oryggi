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

def display_users(user):
    """
    Function to display saved user
    """
    return User.display_user()