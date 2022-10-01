import string
from utils.user import User

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
                user.setUserNameAndPassword(username, password, True)
    
    def login(self, username, password):
        for user in self._users:
            if username == user.getUsername():
                return (password == user.getPassword())
        return False