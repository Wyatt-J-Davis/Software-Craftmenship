import string

class ArithmaticsParser(object):
    
    def evaluate(self, arithmetic):
        if(self.__validateArithmetic(arithmetic)):
            return self.__evaluateResult(arithmetic)
        else: 
            return "Invalid record error"

    def __validateArithmetic(self, arithmetic):
        if(self.__firstAndLastParenthesis(arithmetic)):
            return self.__checkCharacters(arithmetic)
        else:
            return False

    def __firstAndLastParenthesis(self, arithmetic):
        return ((arithmetic[0] == '(') and (arithmetic[-1] == ')'))
    
    def __checkCharacters(self, arithmetic):
        allowed = (string.digits + ')' + '(' + '+' + '-' + '/' + '*' + '**' + ' ')
        return all(c in allowed for c in arithmetic) # Iterate through the arithmetc and make sure it is comprised of valid characters   

    def __evaluateResult(self, arithmetic):
        containsNumbers = self.__getDigitPresent(arithmetic)
        if(containsNumbers == False):
            return 0
        else:
            try:
                return eval(arithmetic)
            except(SyntaxError):
                return "Arithmetic syntax error"
            except(ZeroDivisionError):
                return "Divide by zero error"

    def __getDigitPresent(self, arithmetic):
        containsDigit = False
        for character in arithmetic:
            if character.isdigit():
                containsDigit = True
        return containsDigit
