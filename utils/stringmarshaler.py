from utils.marshaler import ArgumentMarshaler


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