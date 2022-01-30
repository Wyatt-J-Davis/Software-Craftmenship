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
        self.__message = ""
        self.__keyword = ""
        self.__repeatedKeyword = ""
        self.__encodedMessage = ""
        
        
    def writeMessage(self, input):
        self.__message = input
        if((len(self.__message) > 0) and (len(self.__keyword)>0)):
            self.__generateEncodedMessage()
            
    
    def writeKeyword(self, input):
        self.__keyword = input
        if((len(self.__message) > 0) and (len(self.__keyword)>0)):
            self.__generateEncodedMessage()
            

    def readEncodedMessage(self):
        return self.__encodedMessage
    
    def __generateEncodedMessage(self):
        self.__generateRepeatedKeyword()
        self.__generateCipher()
    
    def __generateRepeatedKeyword(self):
        self.__repeatedKeyword = self.__keyword
        for i in range(len(self.__message) - len(self.__keyword)):
            self.__repeatedKeyword += self.__keyword[i%len(self.__keyword)]

    def __generateCipher(self):
        for i in range(len(self.__message)):
            column = alphabet[self.__repeatedKeyword[i]]
            row = alphabet[self.__message[i]]
            self.__encodedMessage = self.__encodedMessage + list(alphabet.keys())[list(alphabet.values()).index((column + row)%len(alphabet))]
        

    


    

        
