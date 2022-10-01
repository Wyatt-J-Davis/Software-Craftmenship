from utils.marshaler import ArgumentMarshaler

class DoubleArgumentMarshaler(ArgumentMarshaler):
    def __init__(self):
        self._doubleArgument = 0.0
    
    def set(self, value):
        if("." in value):
            try:
                self._doubleArgument = float(value)
            except ValueError:
                raise Exception("Error: Argument as double expected.")
        else: 
            raise Exception("Error: Argument as double expected.")
    
    def get(self):
        return self._doubleArgument