class PasswordValid:

    errors=[]

    def length_passw(self, passw):
        if len(passw) < 8:
            self.errors.append('The password must have at least 8 characters long')
            return False
        else:
            return True

    def lowercase_passw(self, passw):
        lowercase_letter=False
        for carac in passw:
            if carac.islower()==True:
                lowercase_letter=True
        if not lowercase_letter:
            self.errors.append('The password must have at least one lowercase')
            return False
        else:
            return True

    def uppercase_passw(self, passw):
        uppercase_letters=False
        for carac in passw:
            if carac.isupper()==True:
                uppercase_letters=True
        if not uppercase_letters:
            self.errors.append('The password must have at least one uppercase')
            return False
        else:
            return True

    def number(self, passw):
        num=False
        for carac in passw:
            if carac.isdigit()== True:
                num=True
        if not num:
            self.errors.append('The password must have at least one number')
            return False
        else:
            return True

    def not_alphanumeric(self, passw):
        if passw.isalnum()==True:
            self.errors.append('The password must have at least a non-alphanumeric character')
            return False
        else:
            return True

    def spaces(self, passw):
        if passw.count(" ") > 0:
            self.errors.append('The password can not contain white in spaces')
            return False
        else:
            return True

    def validate_password(self,passw):
        valid = self.length_passw(passw) and self.lowercase_passw(passw) and self.uppercase_passw(passw) and self.number(passw) and self.not_alphanumeric(passw) and self.spaces(passw)
        return valid