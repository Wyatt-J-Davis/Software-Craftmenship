from random import randint


class TinyMazeSolver(object):

    def solve(self, maze):

        mirrorMaze = []
        xPath = []
        yPath = []

        # Steps to solving
        unsolved = True
        #Start path at zero 
        xPath.append(0)
        yPath.append(0)


        mirrorMaze = maze

        while(unsolved): 
            potentialX = []
            potentialY = []
            # check neighbors for zeros 
         
            # Check to make sure path is not currently on an edge
          
            rightEdge = False
            leftEdge = False
            topEdge = False
            bottomEdge = False
            if(0 == xPath[-1]):
                leftEdge = True
            elif((len(maze[0][:]) - 1) == xPath[-1]):
                rightEdge = True
            if(0 == yPath[-1]):
                topEdge = True
            elif((len(maze[:]) - 1) == yPath[-1]):
                bottomEdge = True
            
            # Check availible moves
            # Left move
            if((not(leftEdge)) and (1 != mirrorMaze[yPath[-1]][xPath[-1] - 1]) and (not(self.__checkForPathCollision(xPath[-1] - 1, yPath[-1],xPath, yPath)))):
                potentialX.append(xPath[-1] - 1)
                potentialY.append(yPath[-1])
            # Right move
            if((not(rightEdge)) and (1 != mirrorMaze[yPath[-1]][xPath[-1] + 1]) and (not(self.__checkForPathCollision((xPath[-1] + 1), yPath[-1],xPath, yPath)))):
                potentialX.append(xPath[-1] + 1)
                potentialY.append(yPath[-1])
            # Up move
            if((not(topEdge)) and (1 != mirrorMaze[yPath[-1] - 1][xPath[-1]]) and (not(self.__checkForPathCollision(xPath[-1], (yPath[-1] - 1),xPath, yPath)))):
                potentialX.append(xPath[-1])
                potentialY.append(yPath[-1] - 1)
            # Down move
            if((not(bottomEdge)) and (1 != mirrorMaze[yPath[-1] + 1][xPath[-1]]) and (not(self.__checkForPathCollision(xPath[-1], (yPath[-1] + 1) ,xPath, yPath)))):
                potentialX.append(xPath[-1])
                potentialY.append(yPath[-1] + 1)

            # to do: choose move at random, if no potenial moves exist then pop the most recent addition to the path and mark it as a wall in the mirror maze.
            
            # Choose move
            if(len(potentialX) > 0):
                # Choose random potential move
                choice = randint(0, (len(potentialX) - 1))
                # Move in that direction
                xPath.append(potentialX[choice])
                yPath.append(potentialY[choice])
            else:
                # Remove that space as a possibility in the mirror maze and move back one in path
                mirrorMaze[yPath[-1]][xPath[-1]] = 1
                xPath.pop()
                yPath.pop()

            # Check to see if path is at end of the maze
            if((yPath[-1] == (len(maze[:]) - 1)) and (xPath[-1] == (len(maze[0][:]) - 1))):
                unsolved = False
                # Draw path and return maze with path
                pathMaze = maze
                for i in range(len(xPath)):
                    pathMaze[yPath[i]][xPath[i]] = 'x'

        return pathMaze
            
            

        

         # choose one of the zeros and go there 

    def __checkForPathCollision(self, xCoordinate, yCoordinate, xPath, yPath):
        collision = False
        for i in range(len(xPath)):
            if((xPath[i] == xCoordinate) and (yPath[i] == yCoordinate)):
                collision = True
        return collision
