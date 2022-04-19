from utils.encryptor import Encryptor
import string

class User(object):
    def __init__(self):
        self._username = ""
        self._password = ""
        self._encryptor = Encryptor()
    
    def getUsername(self):
        return self._encryptor.decrypt(self._username)
    
    def getPassword(self):
        return self._encryptor.decrypt(self._password)
    
    def setUserNameAndPassword(self, username, password, justPassword = False):    
        if(self._verifyUsername(username) and not justPassword):
            self._username = self._encryptor.encrypt(username)
        if(self._verifyPassword(password)):
            self._password = self._encryptor.encrypt(password)

    def _verifyUsername(self,username):
        minimumUsernameLength = 3
        maximumUsernameLength = 31
        allowedInUsername = string.digits + string.ascii_letters
 
        if(minimumUsernameLength > len(username)):
            raise Exception('UsernameTooShort')
        if(maximumUsernameLength < len(username)):
            raise Exception('UsernameTooLong')
        if(not (c in allowedInUsername for c in username)):
            raise Exception('UsernameBadCharacters')
        if(username[0].isdigit()):
            raise Exception('UsernameStartsWithANumber')
        return True

    def _verifyPassword(self, password):
        minimumPasswordLength = 8
        maximumPasswordLength = 255
        specialCharacters = set('!@#$%^&*()-_=+')
        allowedInPassword = string.digits + string.ascii_letters + str(specialCharacters)
        
        if(minimumPasswordLength > len(password)):
            raise Exception('PasswordTooShort')
        if(maximumPasswordLength < len(password)):
            raise Exception('PasswordTooLong')        
        if(not (c in allowedInPassword for c in password)):
            raise Exception('PasswordBadCharacters')
        if(password.isupper()):
            raise Exception('PasswordNoLowerAlpha')
        if(password.islower()):
            raise Exception('PasswordNoUpperAlpha')
        if not any(char.isdigit() for char in password):
            raise Exception('PasswordNoDigit')
        if not any((c in specialCharacters) for c in password):
            raise Exception('PasswordNoSpecialChar')
        if self.getUsername() in password:
            raise Exception('PasswordContainsUsername')
        
        return True