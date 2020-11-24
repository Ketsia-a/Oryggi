import unittest
from credentials import Credentials

class TestUser(unittest.TestCase):
   
    '''
    Test class that defines test cases for the credentials class behaviours.A

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_credential = Credentials("Instagram","ketsia90___","claus2121")

    def test_init(self):

        """
        test_init test case to test if the object is initialized properly
        """
        self.assertEqual(self.new_credential.name,"Instagram")
        self.assertEqual(self.new_credential.account_username,"ketsia90___")
        self.assertEqual(self.new_credential.account_password,"claus2121")    


     
    def test_save_credentials(self):
        '''
        test_save_credentials test case to test if the user object is saved into
         the credentials list
        '''
        self.new_credential.save_credentials()
        self.assertEqual(len(Credentials.credentials_list),1)
    

    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            Credentials.credentials_list = []


    def test_save_multiple_credentials(self):
            '''
            test_save_multiple_credentials to check if we can save multiple credentials
            objects to our credentials_list
            '''
            self.new_credential.save_credentials()
            test_credential = Credentials("Facebook","Karambizi3","blue7887")
            test_credential.save_credentials()
            self.assertEqual(len(Credentials.credentials_list),2)
    
    def test_delete_credential(self):
            '''
            test_delete_credential to test if we can remove a credential from our credentials list
            '''
            self.new_credential.save_credentials()
            test_credential = Credentials("Facebook","Karambizi3","blue7887")
            test_credential.save_credentials()

            self.new_credential.delete_credential()
            self.assertEqual(len(Credentials.credentials_list),1) 
    
    def test_find_credential_by_name(self):
        '''
        test to check if we can find a credential by account name and display information
        '''

        self.new_credential.save_credentials()
        test_credential = Credentials("Facebook","Karambizi3","blue7887") 
        test_credential.save_credentials()

        found_credential = Credentials.find_by_name("Facebook")
        self.assertEqual(found_credential.account_username,test_credential.account_username)
    
    def test_credential_exists(self):
        '''
        test to check if we can return a Boolean  if we cannot find the credential.
        '''

        self.new_credential.save_credentials()
        test_credential = Credentials("Facebook","Karambizi3","blue7887")
        test_credential.save_credentials()

        credentail_exists = Credentials.credential_exist("Karambizi3")
        self.assertTrue(credentail_exists)

    def test_display_all_credential(self):
        '''
        method that returns a list of all credentials saved
        '''
        self.assertEqual(Credentials.display_all_credential(),Credentials.credentials_list)


    def test_password_generate(self):
        """"
        Test case to test if a user can log into their credentials
        """
        password_generate = self.new_credential.password_generate()
        self.assertEqual(len(password_generate),8)

if __name__ == '__main__':
    unittest.main()