import unittest
from utils.MarsRover import MarsRover 

class TestMarsRover(unittest.TestCase):
    def test_rover_orientation(self):
        testRover = MarsRover()
        testRover.command("R")
        testRover.command("R")
        testRover.command("R")
        testRover.command("R")
        assert testRover.getPositionandDirection() == "0:0:N"

    def test_rover_displacement(self):
        testRover = MarsRover()
        testRover.command("MMMRMMML")
        assert testRover.getPositionandDirection() == "3:3:N"
    
    def test_rover_wrap_around(self):
        testRover = MarsRover()
        testRover.command("MMMMMMMMMM")
        assert testRover.getPositionandDirection() == "0:0:N"

if __name__ == '__main__':
    unittest.main()