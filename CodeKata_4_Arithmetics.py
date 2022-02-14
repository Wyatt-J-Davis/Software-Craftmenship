from re import A
from utils.numerics import ArithmaticsParser

ArithmaticsParserA = ArithmaticsParser()

ArithmaticsParserA.writeArithmatic("(((()))")

print(ArithmaticsParserA.getResult())