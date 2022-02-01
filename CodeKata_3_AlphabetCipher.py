from utils.alphabetcipher import AlphabetCipher

# Test code
Cipher = AlphabetCipher()

# Message to send
Cipher.writeMessage("meetmebythetree")

# Keyword
Cipher.writeKeyword("scones")

# Print out encoded message
message = Cipher.readEncodedMessage()
print(message) # We expect "egsgqwtahuiljgs"

# Define unit tests
def testKeyA():
    TestCipher = AlphabetCipher()

    TestCipher.writeMessage("message")

    TestCipher.writeKeyword("a")

    assert TestCipher.readEncodedMessage() == "message"

def testKeyB():
    TestCipher = AlphabetCipher()

    TestCipher.writeMessage("message")

    TestCipher.writeKeyword("b")

    assert TestCipher.readEncodedMessage() == "nfttbhf"

def testKeyUpdate():
    TestCipher = AlphabetCipher()

    TestCipher.writeMessage("message")

    TestCipher.writeKeyword("a")

    assert TestCipher.readEncodedMessage() == "message"

    TestCipher.writeKeyword("b")

    assert TestCipher.readEncodedMessage() == "nfttbhf"

def testMessageUpate():
    TestCipher = AlphabetCipher()

    TestCipher.writeMessage("message")

    TestCipher.writeKeyword("a")

    assert TestCipher.readEncodedMessage() == "message"

    TestCipher.writeMessage("apple")

    assert TestCipher.readEncodedMessage() == "apple"


# Run unit tests
testKeyA()
testKeyB()
testKeyUpdate()
testMessageUpate()