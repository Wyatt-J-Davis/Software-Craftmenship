from utils.marshaler import ArgumentMarshaler

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