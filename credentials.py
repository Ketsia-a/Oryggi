import string
import random
from user import User

class Credentials:
    """
    class that generates new instances of accounts
    """
    credentials_list = []

    def __init__(self, name,account_username, account_password):
        """
        Args:
            name:first name on your account
            account_username:user name on your account
            account_password: new password generated for that account
        """
        self.name = name 
        self.account_username = account_username 
        self.account_password = account_password
    
    def save_credentials(self):

        '''
        save_credental method saves credential objects into credential_list
        '''

        Credentials.credentials_list.append(self)
    
    @classmethod
    def verify_user(cls,username, password):
        """
        method to verify whether the user is our user_list or not
        """
        actual_user = ""
        for user in User.user_list:
            if(user.username == username and user.password == password):
                actual_user == user.username
        return actual_user    

    def delete_credential(self):

        '''
        delete_credential method deletes a saved credential from the credentials_list
        '''

        Credentials.credentials_list.remove(self)    

    @classmethod    
    def find_by_name(cls,name):
        '''
        Method that takes in an account name  and returns an account username that matches that account name.

        Args:
            Account name: Account name to search for
        Returns :
            Username of person that matches the account name.
        '''

        for credential in cls.credentials_list:
            if credential.name == name:
                return credential 

    @classmethod
    def password_generate(cls):
        """
        Generate a random password using string of letters and digits and special characters
        """
        size = 8
        charact = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(charact)for i in range(size))
        return password         

    @classmethod
    def credential_exist(cls,account_username):
        '''
         Method that checks if a credential exists from the credential list.
        '''
        for credential in cls.credentials_list:
            if credential.account_username == account_username:
                return True

        return False

    @classmethod
    def display_all_credential(cls):
        '''
        method that returns the credential list
        '''

        return cls.credentials_list

    
    