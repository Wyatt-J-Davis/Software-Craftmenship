import string

class UserManager(object):
    def __init__(self):
        self._users = []
    
    def recordNewUser(self, username, password):
        newUser = User()
        newUser.setUserNameAndPassword(username, password)
        self._users.append(newUser)

    def getUser(self, username):
        userPresent = False
        for user in self._users:
            if username == user.getUsername():
                userPresent = True
        return userPresent


class User(object):
    def __init__(self):
        self._username = ""
        self._password = ""
    
    def getUsername(self):
        return self._username
    
    def setUserNameAndPassword(self, username, password):
        self._verifyUsername(username)
        self._username = username
        self._verifyPassword(password)
        self._password = password

    def _verifyUsername(self,username):
        if(3 > len(username)):
            raise ValueError('UsernameTooShort')
        if(31 < len(username)):
            raise ValueError('UsernameTooLong')
        allowed = (string.digits + string.ascii_letters)
        if(not (c in allowed for c in username)):
            raise ValueError('UsernameBadCharacters')
        if(username[0].isdigit()):
            raise ValueError('UsernameStartsWithANumber')

    def _verifyPassword(self,password):
        if(8 > len(password)):
            raise ValueError('PasswordTooShort')
        if(255 < len(password)):
            raise ValueError('PasswordTooLong')        
        allowed = (string.digits + string.ascii_letters + '!' + '@' + '#' + '$' + '%' + '^' + '&' + '*' + '(' + ')' + '-' + '_' + '=' + '+')
        if(not (c in allowed for c in password)):
            raise ValueError('PasswordBadCharacters')
        if(password.isupper()):
            raise ValueError('PasswordNoLowerAlpha')
        if(password.islower()):
            raise ValueError('PasswordNoUpperAlpha')
        if not any(char.isdigit() for char in password):
            raise ValueError('PasswordNoDigit')
        specialCharacters = set('!@#$%^&*()-_=+')
        if not any((c in specialCharacters) for c in password):
            raise ValueError('PasswordNoSpecialChar')
        if self._username in password:
            raise ValueError('PasswordContainsUsername')

        