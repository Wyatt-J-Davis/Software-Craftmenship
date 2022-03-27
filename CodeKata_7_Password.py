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
        assert e == 'UsernameTooShort'

def testUserNameTooLong():
    testUserManager = UserManager()
    try:
        testUserManager.recordNewUser('Wyattttttttttttttttttttttttttttt','Tortise85&70')
    except Exception as e:
        assert e == 'UsernameTooLong'

def testUserNameBadCharacter():
    testUserManager = UserManager()
    try:
        testUserManager.recordNewUser('Wyatt%','Tortise85&70')
    except Exception as e:
        assert e == 'UsernameBadCharacters'

def testUserNameStartingWithNumber():
    testUserManager = UserManager()
    try:
        testUserManager.recordNewUser('5Wyatt','Tortise85&70')
    except Exception as e:
        assert e == 'UsernameStartsWithANumber'

def testPasswordTooShort():
    testUserManager = UserManager()
    try:
        testUserManager.recordNewUser('Wyatt','T85&')
    except Exception as e:
        assert e == 'PasswordTooShort'

def testPasswordTooLong():
    testUserManager = UserManager()
    try:
        testUserManager.recordNewUser('Wyatt','Tortise85&70000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    except Exception as e:
        assert e == 'PasswordTooLong'

def testPasswordBadCharacters():
    testUserManager = UserManager()
    try:
        testUserManager.recordNewUser('Wyatt','Tortise85&70~')
    except Exception as e:
        assert e == 'PasswordBadCharacters'

def testPasswordNoLowerAlpha():
    testUserManager = UserManager()
    try:
        testUserManager.recordNewUser('Wyatt','TORTISE85&70')
    except Exception as e:
        assert e == 'PasswordNoLowerAlpha'

def testPasswordNoUpperAlpha():
    testUserManager = UserManager()
    try:
        testUserManager.recordNewUser('Wyatt','tortise85&70')
    except Exception as e:
        assert e == 'PasswordNoLowerAlpha'

def testPasswordNoDigit():
    testUserManager = UserManager()
    try:
        testUserManager.recordNewUser('Wyatt','Tortise&')
    except Exception as e:
        assert e == 'PasswordNoDigit'

def testPasswordNoSpecialChar():
    testUserManager = UserManager()
    try:
        testUserManager.recordNewUser('Wyatt','Tortise8570')
    except Exception as e:
        assert e == 'PasswordNoSpecialChar'

def testPasswordContainsUsername():
    testUserManager = UserManager()
    try:
        testUserManager.recordNewUser('Wyatt','TortiseWyatt8570')
    except Exception as e:
        assert e == 'PasswordContainsUsername'