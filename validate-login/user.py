class UserValid:
    
    errors=[]
    
    def length(self,username):
        if len(username) < 6:
            self.errors.append('Username must contain at least 6 characters')
            return False

        elif len(username) > 12:
            self.errors.append('Username must contain max 12 characterers')
            return False

        else:
            return True
    
    def alphanumeric(self,username):
        if username.isalnum()== False:
            self.errors.append('Username can contain only letters and numbers')
            return False
        else:
            return True

    def validate_user(self,username):
        valid=self.length(username) and self.alphanumeric(username)
        return valid