from utils.alphabetcipher import AlphabetCipher

# Test code
CipherA = AlphabetCipher()

# Message to send
CipherA.writeMessage("meetmebythetree")

# Keyword
CipherA.writeKeyword("scones")

# Print out encoded message
message = CipherA.readEncodedMessage()
print(message) # We expect "egsgqwtahuiljgs"

#Create second cipher object to decode message sent by first
CipherB = AlphabetCipher()

# Write keyword
CipherB.writeKeyword("scones")

# Second CipherB recieves message encoded by CipherA
CipherB.recieveMessage(message)

decodedMessage = CipherB.readDecodedMessage()
print(decodedMessage)

CipherB.writeMessage("seeyoubythetree")

message = CipherB.readEncodedMessage()

print(message)

CipherA.recieveMessage(message)

recievedMessage = CipherA.readDecodedMessage()

print(recievedMessage)

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