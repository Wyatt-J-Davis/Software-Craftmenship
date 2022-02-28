
class TinyMazeSolver(object):

    def __init__(self):
        __mirrorMaze = []
        __xPath = []
        __yPath = []

    def solve(maze, self):
        # Steps to solving
        unsolved = True
        #Start path at zero 
        self.xPath.append(0)
        self.yPath.append(0)


        self.__mirrorMaze = maze

        while(unsolved): 
            potentialX = []
            potentialY = []
         # check neighbors for zeros 
         
         # Check to make sure path is not currently on an edge
            if(0 == self.__xPath[-1]):
                leftEdge = True
            elif((len(maze[0][:]) - 1) == self.__xPath[-1]):
                rightEdge = True
            if(0 == self.__yPath[-1]):
                topEdge = True
            elif((len(maze[:]) - 1) == self.__yPath[-1]):
                bottomEdge = True
            
            # Check availible moves
            # Left move
            if(~leftEdge and (0 == maze[self.__yPath[-1]][self.__xPath[-1] - 1]) and ~self.__checkForPathCollision(self.__xPath[-1] - 1, self.__yPath[-1])):
                potentialX.append(self.__xPath[-1] - 1)
                potentialY.append(self.__yPath[-1])
            # Right move
            if(~rightEdge and (0 == maze[self.__yPath[-1]][self.__xPath[-1] + 1]) and ~self.__checkForPathCollision(self.__xPath[-1] + 1, self.__yPath[-1])):
                potentialX.append(self.__xPath[-1] + 1)
                potentialY.append(self.__yPath[-1])
            # Up move
            if(~topEdge and (0 == maze[self.__yPath[-1] - 1][self.__xPath[-1]]) and ~self.__checkForPathCollision(self.__xPath[-1], self.__yPath[-1] - 1)):
                potentialX.append(self.__xPath[-1])
                potentialY.append(self.__yPath[-1] - 1)
            # Down move
            if(~topEdge and (0 == maze[self.__yPath[-1] + 1][self.__xPath[-1]]) and ~self.__checkForPathCollision(self.__xPath[-1], self.__yPath[-1] + 1)):
                potentialX.append(self.__xPath[-1])
                potentialY.append(self.__yPath[-1] + 1)

            # to do: choose move at random, if no potenial moves exist then pop the most recent addition to the path and mark it as a wall in the mirror maze.

            

        


         # choose one of the zeros and go there 

    def __checkForPathCollision(xCoordinate, yCoordinate, self):
        for i in range(len(self.__xPath)):
            if((self.__xPath[i] == xCoordinate) and (self.__yPath[i] == yCoordinate)):
                return True
        return False
