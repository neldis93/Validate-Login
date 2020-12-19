from time import time
from getpass import getpass
from user import UserValid
from password import PasswordValid
from email import EmailValid 

user_validator = UserValid()
pass_validator = PasswordValid()
email_validator = EmailValid()

def main_login(): 
    time_init= time()        
    correct= False

    while (correct==False):
        name = input('Enter your Username: ')
        if not user_validator.validate_user(name):
            for error in user_validator.errors:
                print (error)
                correct=False
                user_validator.errors.remove(error)           
        else:
            correct=True
            

    while (correct==True):
        email= input('Enter your Email: ')
        if not email_validator.validate_email(email):
            for error in email_validator.errors:
                print(error)
                correct= True
                email_validator.errors.remove(error)
        else:
            correct= False

    while (correct==False):        
        password= getpass('Enter your Password: ')
        if not pass_validator.validate_password(password):
            for error in pass_validator.errors:
                print (error)
                correct=False
                pass_validator.errors.remove(error)
        else:
            correct=True

    print(f'\nWelcome at system {name}')

    time_final= time() - time_init
    print(f"Running time: {time_final}")

