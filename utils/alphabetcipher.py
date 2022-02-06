alphabet = {
    "a":0,
    "b":1,
    "c":2,
    "d":3,
    "e":4,
    "f":5,
    "g":6,
    "h":7,
    "i":8,
    "j":9,
    "k":10,
    "l":11,
    "m":12,
    "n":13,
    "o":14,
    "p":15,
    "q":16,
    "r":17,
    "s":18,
    "t":19,
    "u":20,
    "v":21,
    "w":22,
    "x":23,
    "y":24,
    "z":25
}

class AlphabetCipher(object):
    def __init__(self):
        self.__messageToSend = ""
        self.__messageToRecieve = ""
        self.__keyword = ""
        self.__encodedMessage = ""
        self.__decodedMessage = ""
        
    def readEncodedMessage(self):
        return self.__encodedMessage
    
    def readDecodedMessage(self):
        return self.__decodedMessage

    def writeMessage(self, message):
        self.__messageToSend = message
        if(len(self.__messageToSend) > 0 and len(self.__keyword) > 0):
            self.__encode()
    
    def recieveMessage(self, message):
        self.__messageToRecieve = message
        if(len(self.__messageToRecieve) > 0 and len(self.__keyword) > 0):
            self.__decode()
            
    def writeKeyword(self, keyword):
        self.__keyword = keyword
        if(len(self.__messageToSend) > 0 and len(self.__keyword) > 0):
            self.__encode()
        if(len(self.__messageToRecieve) > 0 and len(self.__keyword) > 0):
            self.__decode()
    
    def __encode(self):
        self.__encodedMessage = ""
        for i in range(len(self.__messageToSend)):
            keywordIndex = alphabet[self.__keyword[i%len(self.__keyword)]] 
            messageIndex = alphabet[self.__messageToSend[i]]
            self.__encodedMessage = self.__encodedMessage + list(alphabet.keys())[list(alphabet.values()).index((keywordIndex + messageIndex)%len(alphabet))]

    def __decode(self):
        self.__encodedMessage = ""
        for i in range(len(self.__messageToRecieve)):
            keywordIndex = alphabet[self.__keyword[i%len(self.__keyword)]] 
            recieveMessageIndex = alphabet[self.__messageToRecieve[i]]
            self.__decodedMessage = self.__decodedMessage + list(alphabet.keys())[list(alphabet.values()).index((recieveMessageIndex - keywordIndex)%len(alphabet))]