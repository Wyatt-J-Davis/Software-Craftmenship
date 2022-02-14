class ArithmaticsParser(object):
    
    def __init__(self):
        self.__arithmetic = ""
        self.__validArithmetic = True
        self.__result = ""

    def writeArithmatic(self, arithmetic):
        self.__validArithmetic = self.__validateArithmatic(arithmetic)
        if(self.__validArithmetic):
            self.__arithmetic = arithmetic
        else:
            print("Invalid input. Try again.")

    def getResult(self):
        if(self.__validArithmetic):
            self.__evaluateResult()
            return self.__result
        else:
            print("Unable to evaluate result due to invalid input. Input valid arithmatic and try again.")

    def __validateArithmatic(self, arithmetic):
        valid = self.__firstAndLastParenthesis(arithmetic)
        if(True == valid):
            valid = self.__countParenthesis(arithmetic)
        return valid

    def __firstAndLastParenthesis(self, arithmetic):
        if((arithmetic[0] == '(') and (arithmetic[-1] == ')')):
            return True
        else:
            return False
        
    def __countParenthesis(self, arithmetic):
        lefthandParenthesis = 0
        righthandParenthesis = 0
        valid = True
        for character in arithmetic: 
            if (character == '('):
                lefthandParenthesis += 1
            elif(character ==  ')'):
                righthandParenthesis += 1
            if(righthandParenthesis > lefthandParenthesis):
                valid = False
        if(righthandParenthesis != lefthandParenthesis):
            valid = False
        
        return valid

    def __evaluateResult(self):
        containsNumbers = self.__getDigitPresent()
        if(containsNumbers == False):
            self.__result = 0
        else:
            self.__result = eval(self.__arithmetic)

    def __getDigitPresent(self):
        containsDigit = False
        for character in self.__arithmetic:
            if character.isdigit():
                containsDigit = True
        
        return containsDigit




    #def calculateResult(self):


