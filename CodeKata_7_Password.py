from utils.password import UserManager

def testNewUser():
    testUserManager = UserManager()
    testUserManager.recordNewUser('WyattD','Tortise85&70')
    userExists = testUserManager.getUser('WyattD')
    assert True == userExists

def testUserNameTooShort():
    testUserManager = UserManager()
    try:
        testUserManager.recordNewUser('Wya','Tortise85&70')
    except Exception as e:
        assert str(e) == 'UsernameTooShort'

def testUserNameTooLong():
    testUserManager = UserManager()
    try:
        testUserManager.recordNewUser('Wyattttttttttttttttttttttttttttttt','Tortise85&70')
    except Exception as e:
        assert str(e) == 'UsernameTooLong'

def testUserNameBadCharacter():
    testUserManager = UserManager()
    try:
        testUserManager.recordNewUser('Wyatt%','Tortise85&70')
    except Exception as e:
        assert str(e) == 'UsernameBadCharacters'

def testUserNameStartingWithNumber():
    testUserManager = UserManager()
    try:
        testUserManager.recordNewUser('5Wyatt','Tortise85&70')
    except Exception as e:
        assert str(e) == 'UsernameStartsWithANumber'
        
def testPasswordTooShort():
    testUserManager = UserManager()
    try:
        testUserManager.recordNewUser('Wyatt','T85&')
    except Exception as e:
        assert str(e) == 'PasswordTooShort'

def testPasswordTooLong():
    testUserManager = UserManager()
    try:
        testUserManager.recordNewUser('Wyatt','Tortise85&70000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    except Exception as e:
        assert str(e) == 'PasswordTooLong'

def testPasswordBadCharacters():
    testUserManager = UserManager()
    try:
        testUserManager.recordNewUser('Wyatt','Tortise85&70~')
    except Exception as e:
        assert str(e) == 'PasswordBadCharacters'

def testPasswordNoLowerAlpha():
    testUserManager = UserManager()
    try:
        testUserManager.recordNewUser('Wyatt','TORTISE85&70')
    except Exception as e:
        assert str(e) == 'PasswordNoLowerAlpha'

def testPasswordNoUpperAlpha():
    testUserManager = UserManager()
    try:
        testUserManager.recordNewUser('Wyatt','tortise85&70')
    except Exception as e:
        assert str(e) == 'PasswordNoUpperAlpha'

def testPasswordNoDigit():
    testUserManager = UserManager()
    try:
        testUserManager.recordNewUser('Wyatt','Tortise&')
    except Exception as e:
        assert str(e) == 'PasswordNoDigit'

def testPasswordNoSpecialChar():
    testUserManager = UserManager()
    try:
        testUserManager.recordNewUser('Wyatt','Tortise8570')
    except Exception as e:
        assert str(e) == 'PasswordNoSpecialChar'

def testPasswordContainsUsername():
    testUserManager = UserManager()
    try:
        testUserManager.recordNewUser('Wyatt','TortiseWyatt85&70')
    except Exception as e:
        assert str(e) == 'PasswordContainsUsername'


testNewUser()
testUserNameTooShort()
testPasswordTooLong()
testUserNameBadCharacter()
testUserNameStartingWithNumber()
testPasswordTooShort()
testPasswordTooLong()
testPasswordBadCharacters()
testPasswordNoLowerAlpha()
testPasswordNoUpperAlpha()
testPasswordNoDigit()
testPasswordNoSpecialChar()
testPasswordContainsUsername()