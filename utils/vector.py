compass = {
    "N":0,
    "E":1,
    "S":2,
    "W":3,
}

class Vector(object):
    def __init__(self):
        self._loc = [0,0]
        self._direction = compass("N")

    def displaceX(self, xDisplacement):
        self._loc[0] += xDisplacement

    def displaceY(self, yDisplacement):
        self._loc[1] += yDisplacement
    
    def rotate(self, rotation):
        self._direction += rotation

    def getLoc(self):
        return self._loc
    
    def get_direction(self):
        return compass(self._direction % len(compass))