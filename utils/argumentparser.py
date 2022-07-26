from utils.booleanmarshaler import BooleanArgumentMarshaler
from utils.stringmarshaler import StringArgumentMarshaler
from utils.integermarshaler import IntegerArgumentMarshaler
from utils.doublemarshaler import DoubleArgumentMarshaler

class ArgParser(object):
    def __init__(self, schema, args):
        self._schema = schema
        self._args = args
        self._passedArguemntVariables = []
        self._marshalers = {}

        self._parseSchema()
        self._parseArgumentStrings()
    
    def usage(self):
        if(len(self._schema) > 0):
            return "-" + str(self._schema) + "-"
        else:
            return ""

    def cardinality(self):
        return len(self._passedArguemntVariables)
    
    def getArgument(self, argument):
        return self._marshalers[argument].get()

    def _parseSchema(self):
        for element in self._schema:
            self._parseSchemaElement(element)
    
    def _parseArgumentStrings(self):
        for index, arg in enumerate(self._args):
            if(arg[0] == '-'):
                self._marshalers[arg[1:]].set(self._args[index + 1])
                self._passedArguemntVariables.append(arg[1:])
        
    def _parseSchemaElement(self, element):
        elementTail = element[1:]
        if(0 == len(elementTail)):
            self._marshalers.update({element[0]: BooleanArgumentMarshaler()})
        elif('*' == elementTail):
            self._marshalers.update({element[0]: StringArgumentMarshaler()})
        elif('#' == elementTail):
            self._marshalers.update({element[0]: IntegerArgumentMarshaler()})
        elif('##' == elementTail):
            self._marshalers.update({element[0]: DoubleArgumentMarshaler()})
        else:
            raise Exception("Invalid schema element.")