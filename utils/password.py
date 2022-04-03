import string

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

class User(object):
    def __init__(self):
        self._username = ""
        self._password = ""
    
    def getUsername(self):
        return self._username
    
    def setUserNameAndPassword(self, username, password):
        self._verifyUsernameAndPassword(username,password)
        self._username = username
        self._password = password

    def _verifyUsernameAndPassword(self,username,password):
        if(3 > len(username)):
            raise Exception('UsernameTooShort')
        if(31 < len(username)):
            raise Exception('UsernameTooLong')
        allowed = (string.digits + string.ascii_letters)
        if(not (c in allowed for c in username)):
            raise Exception('UsernameBadCharacters')
        if(username[0].isdigit()):
            raise Exception('UsernameStartsWithANumber')
        if(8 > len(password)):
            raise Exception('PasswordTooShort')
        if(255 < len(password)):
            raise Exception('PasswordTooLong')        
        allowed = (string.digits + string.ascii_letters + '!' + '@' + '#' + '$' + '%' + '^' + '&' + '*' + '(' + ')' + '-' + '_' + '=' + '+')
        if(not (c in allowed for c in password)):
            raise Exception('PasswordBadCharacters')
        if(password.isupper()):
            raise Exception('PasswordNoLowerAlpha')
        if(password.islower()):
            raise Exception('PasswordNoUpperAlpha')
        if not any(char.isdigit() for char in password):
            raise Exception('PasswordNoDigit')
        specialCharacters = set('!@#$%^&*()-_=+')
        if not any((c in specialCharacters) for c in password):
            raise Exception('PasswordNoSpecialChar')
        if username in password:
            raise Exception('PasswordContainsUsername')