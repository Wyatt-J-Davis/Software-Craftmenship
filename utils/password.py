import string
from utils.encryptor import Encryptor

class UserManager(object):
    def __init__(self):
        self._users = []
    
    def recordNewUser(self, username, password):
        newUser = User()
        newUser.setUserNameAndPassword(username, password)
        self._users.append(newUser)

    def getUser(self, username):
        for user in self._users:
            if username == user.getUsername():
                return True
        return False
    
    def setPassword(self, username, password):
        for user in self._users:
            if username == user.getUsername():
                user.setUserNameAndPassword(username, password)
    
    def login(self, username, password):
        for user in self._users:
            if username == user.getUsername():
                return (password == user.getPassword())
        return False
            

class User(object):
    def __init__(self):
        self._username = ""
        self._password = ""
        self._encryptor = Encryptor()
    
    def getUsername(self):
        return self._encryptor.decrypt(self._username)
    
    def getPassword(self):
        return self._encryptor.decrypt(self._password)
    
    def setUserNameAndPassword(self, username, password):    
        if(self._verifyUsernameAndPassword(username,password)):
            self._username = self._encryptor.encrypt(username)
            self._password = self._encryptor.encrypt(password)

    def _verifyUsernameAndPassword(self,username,password):
        minimumUsernameLength = 3
        maximumUsernameLength = 31
        minimumPasswordLength = 8
        maximumPasswordLength = 255
        allowedInUsername = string.digits + string.ascii_letters
        specialCharacters = set('!@#$%^&*()-_=+')
        allowedInPassword = string.digits + string.ascii_letters + str(specialCharacters) 
        
        if(minimumUsernameLength > len(username)):
            raise Exception('UsernameTooShort')
        if(maximumUsernameLength < len(username)):
            raise Exception('UsernameTooLong')
        if(not (c in allowedInUsername for c in username)):
            raise Exception('UsernameBadCharacters')
        if(username[0].isdigit()):
            raise Exception('UsernameStartsWithANumber')
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
        if username in password:
            raise Exception('PasswordContainsUsername')

        return True

    