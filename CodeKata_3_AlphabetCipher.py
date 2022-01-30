from utils.alphabetcipher import AlphabetCipher

# Test code

Cipher = AlphabetCipher()

# Message to send
Cipher.writeMessage("meetmebythetree")

# Keyword
Cipher.writeKeyword("scones")

#Print out encoded message
cipher = Cipher.readEncodedMessage()
print(cipher) # We expect "egsgqwtahuiljgs"