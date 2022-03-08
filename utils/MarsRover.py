compass = ['N', 'E', 'S', 'W']
xGrid = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
yGrid = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

class MarsRover(object):
    
    def __init__(self):
        self.__orientation = 0
        self.__xDisplacement = 0
        self.__yDisplacement = 0
    
    def Command(self, command):
        for subcommand in command:
            match subcommand:
                case "M":
                    self.__Move()
                case "L":
                    self.__orientation -= 1
                case "R":
                    self.__orientation += 1 
                case _:
                    print(f"{subcommand} is not a valid command. Use M, L, or R to command the rover.")
    
    def __Move(self):
        match compass[self.__orientation % len(compass)]:
            case 'N':
                self.__yDisplacement += 1
            case 'E':
                self.__xDisplacement += 1
            case 'S':
                self.__yDisplacement -= 1
            case 'W':
                self.__xDisplacement -= 1
    
    def getPositionandDirection(self):
        x = xGrid[self.__xDisplacement % len(xGrid)] # Use mod operation to enforce wrap-around for positions and direction
        y = yGrid[self.__yDisplacement % len(yGrid)]
        direction = compass[self.__orientation % len(compass)]
        
        return f"{x}:{y}:{direction}"
    
