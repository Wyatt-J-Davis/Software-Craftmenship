from utils.MarsRover import MarsRover

# Test code

# Initialze rovers
RoverAlpha = MarsRover()
RoverBeta = MarsRover()

# Command rovers
RoverAlpha.Command("MMMMRMMM")
RoverBeta.Command("MMMM")

# Output positions and orientations of both rovers
print(RoverAlpha.getPositionandDirection())
print(RoverBeta.getPositionandDirection())

# Continue to command rovers
RoverAlpha.Command("MR")
RoverBeta.Command("ML")

# Output positions and orientations of both rovers
print(RoverAlpha.getPositionandDirection())
print(RoverBeta.getPositionandDirection())


# Create unit tests:
def test_rover_orientation():
    TestRover = MarsRover()
    
    TestRover.Command("R")
    assert TestRover.getPositionandDirection() == "0:0:E"
    
    TestRover.Command("R")
    assert TestRover.getPositionandDirection() == "0:0:S"

    TestRover.Command("R")
    assert TestRover.getPositionandDirection() == "0:0:W"

    TestRover.Command("R")
    assert TestRover.getPositionandDirection() == "0:0:N"


def test_rover_displacement():
    TestRover = MarsRover()

    TestRover.Command("MMMRMMML")
    assert TestRover.getPositionandDirection() == "3:3:N"


def test_rover_wrap_around():
    TestRover = MarsRover()
    
    TestRover.Command("MMMMMMMMMM")
    assert TestRover.getPositionandDirection() == "0:0:N"

    TestRover.Command("RMMMMMMMMMM")
    assert TestRover.getPositionandDirection() == "0:0:E"


# Tests will throw an assert error if not passed
test_rover_orientation()
test_rover_displacement()
test_rover_wrap_around()
