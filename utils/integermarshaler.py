from utils.marshaler import ArgumentMarshaler

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