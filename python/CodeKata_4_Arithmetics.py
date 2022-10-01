from utils.numerics import ArithmaticsParser

# Test simple evaluation
ArithmaticsParserA = ArithmaticsParser()
print(ArithmaticsParserA.evaluate("(5 * 5)"))

# Define unit tests 
def evaluateTestA():
    TestParser = ArithmaticsParser()
    assert TestParser.evaluate('( 1 + ( ( 2 + 3 ) * (4 * 5) ) )') == 101

def evaluateTestB():
    TestParser = ArithmaticsParser()
    assert TestParser.evaluate('( 5 * ( 4 * ( 3 * ( 2 * ( 1 * 9 ) / 8 - 7 ) + 6 ) ) )') == -165

def evaluateTestC():
    TestParser = ArithmaticsParser()
    assert TestParser.evaluate('((()()))') == 0

def evaluateTestD():
    TestParser = ArithmaticsParser()
    assert TestParser.evaluate('3 + ( 2 * 1 )') == "Invalid record error"

def evaluateTestE():
    TestParser = ArithmaticsParser()
    assert TestParser.evaluate('((3 + ( 2 * 1 ))') == "Arithmetic syntax error"

def evaluateTestF():
    TestParser = ArithmaticsParser()
    assert TestParser.evaluate('(3 + ( 2 / 0 ))') == "Divide by zero error"

# Execute unit tests
evaluateTestA()
evaluateTestB()
evaluateTestC()
evaluateTestE()
evaluateTestF()

