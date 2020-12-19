import re

class EmailValid:
    errors=[]

    def clean_email(self,email):
        if re.match('^[(a-z0-9\_\-\.)]+@[(a-z0-9\_\-\.)]+\.[(a-z)]{2,15}$',email.lower()):
            return True
        else:
            self.errors.append('Error, please enter a email valid')
            return False

    def validate_email(self,email):
        valid = self.clean_email(email)
        return valid
        