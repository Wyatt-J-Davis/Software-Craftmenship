from tokenize import Double

class ArgParser(object):
    def __init__(self, schema, args):
        self._schema = schema
        self._args = args
        self._marshalers = {}

        self._parseSchema()
        self._parseArgumentStrings()
    
    def getArgument(self, argument):
        return self._marshalers[argument].get()

    def _parseSchema(self):
        for element in self._schema:
            self._parseSchemaElement(element)
    
    def _parseArgumentStrings(self):
        marshalerList = list(self._marshalers)
        for index, argument in enumerate(self._args):
            self._marshalers[marshalerList[index]].set(argument)
        
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

# Marshaler classes
class ArgumentMarshaler:
    def set(self, value):
        pass
    
    def get(self):
        pass


class BooleanArgumentMarshaler(ArgumentMarshaler):
    def __init__(self):
        self._booleanArgument = False
    
    def set(self, value):
        if("False" == value):
            self._booleanArgument = False
        elif("True" == value):
            self._booleanArgument = True
        else: 
            raise Exception("Error: Argument as boolean value expected.")
    
    def get(self):
        return self._booleanArgument 

class StringArgumentMarshaler(ArgumentMarshaler):
    def __init__(self):
        self._stringArgument = ""
    
    def set(self, value):
        if(None is not value):
            self._stringArgument = value
        else: 
            raise Exception("Error: Argument as string value expected.")
    
    def get(self):
        return self._stringArgument 

class IntegerArgumentMarshaler(ArgumentMarshaler):
    def __init__(self):
        self._integerArgument = 0
    
    def set(self, value):
        if(not("." in value)):
            try:
                self._integerArgument = int(value)
            except ValueError:
                raise Exception("Error: Argument as integer expected.")
        else: 
            raise Exception("Error: Argument as integer expected.")
    
    def get(self):
        return self._integerArgument

class DoubleArgumentMarshaler(ArgumentMarshaler):
    def __init__(self):
        self._doubleArgument = 0.0
    
    def set(self, value):
        if("." in value):
            try:
                self._doubleArgument = Double(value)
            except ValueError:
                raise Exception("Error: Argument as double expected.")
        else: 
            raise Exception("Error: Argument as double expected.")
    
    def get(self):
        return self._doubleArgument