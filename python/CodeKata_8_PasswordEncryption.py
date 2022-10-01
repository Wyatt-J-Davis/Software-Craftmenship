from cryptography.fernet import Fernet
from utils.password import UserManager

def learningTest():
    value = "Encrypt Me"  
    key = Fernet.generate_key()
    encryptedValue = Fernet(key).encrypt(bytes(value, encoding='utf-8'))
    assert value == Fernet(key).decrypt(encryptedValue).decode("utf-8")

def testNewUser():
    testUserManager = UserManager()
    testUserManager.recordNewUser('WyattD','Tortise85&70')
    userExists = testUserManager.getUser('WyattD')
    assert True == userExists

def testSetPassword():
    testUserManager = UserManager()
    testUserManager.recordNewUser('WyattD','Tortise85&70')
    testUserManager.setPassword('WyattD', 'NewPassword123%')
    assert True == testUserManager.login('WyattD', 'NewPassword123%')

def testLoginFail():
    testUserManager = UserManager()
    testUserManager.recordNewUser('WyattD','Tortise85&70')
    assert False == testUserManager.login('WyattD', 'Tortise85&71%')

learningTest()
testNewUser()
testSetPassword()
testLoginFail()