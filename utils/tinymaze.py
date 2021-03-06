from random import randint


class TinyMazeSolver(object):

    def solve(self, maze):
        mirrorMaze = []
        xPath = []
        yPath = []
        unsolved = True
        xPath.append(0)
        yPath.append(0)
        mirrorMaze = maze
        
        while(unsolved): 
            rightEdge, leftEdge, topEdge, bottomEdge = self.__checkForEdges(maze, xPath, yPath)
            potentialX, potentialY = self.__checkAvailibleMoves(rightEdge, leftEdge, topEdge, bottomEdge, mirrorMaze, xPath, yPath)
            self.__chooseMove(xPath, yPath, potentialX, potentialY, mirrorMaze)
            unsolved, pathMaze = self.__checkIfSolved(maze, unsolved, xPath, yPath)

        return pathMaze

    def __checkForEdges(self, maze, xPath, yPath):
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

        return rightEdge, leftEdge, topEdge, bottomEdge

    
    def __checkAvailibleMoves(self, rightEdge, leftEdge, topEdge, bottomEdge, mirrorMaze, xPath, yPath):
        potentialX = []
        potentialY = []
        
        if((not(leftEdge)) and (1 != mirrorMaze[yPath[-1]][xPath[-1] - 1]) and (not(self.__checkForPathCollision(xPath[-1] - 1, yPath[-1],xPath, yPath)))):
            potentialX.append(xPath[-1] - 1)
            potentialY.append(yPath[-1])
        
        if((not(rightEdge)) and (1 != mirrorMaze[yPath[-1]][xPath[-1] + 1]) and (not(self.__checkForPathCollision((xPath[-1] + 1), yPath[-1],xPath, yPath)))):
            potentialX.append(xPath[-1] + 1)
            potentialY.append(yPath[-1])
            
        if((not(topEdge)) and (1 != mirrorMaze[yPath[-1] - 1][xPath[-1]]) and (not(self.__checkForPathCollision(xPath[-1], (yPath[-1] - 1),xPath, yPath)))):
            potentialX.append(xPath[-1])
            potentialY.append(yPath[-1] - 1)
        
        if((not(bottomEdge)) and (1 != mirrorMaze[yPath[-1] + 1][xPath[-1]]) and (not(self.__checkForPathCollision(xPath[-1], (yPath[-1] + 1) ,xPath, yPath)))):
            potentialX.append(xPath[-1])
            potentialY.append(yPath[-1] + 1)
        
        return potentialX, potentialY

    def __checkForPathCollision(self, xCoordinate, yCoordinate, xPath, yPath):
        collision = False
        for i in range(len(xPath)):
            if((xPath[i] == xCoordinate) and (yPath[i] == yCoordinate)):
                collision = True
        return collision

    def __chooseMove(self, xPath, yPath, potentialX, potentialY, mirrorMaze):
        if(len(potentialX) > 0):
                choice = randint(0, (len(potentialX) - 1))
                xPath.append(potentialX[choice])
                yPath.append(potentialY[choice])
        else:
            mirrorMaze[yPath[-1]][xPath[-1]] = 1
            xPath.pop()
            yPath.pop()
    
    def __checkIfSolved(self, maze, unsolved, xPath, yPath):
            if((yPath[-1] == (len(maze[:]) - 1)) and (xPath[-1] == (len(maze[0][:]) - 1))):
                unsolved = False
                pathMaze = maze
                for i in range(len(xPath)):
                    pathMaze[yPath[i]][xPath[i]] = 'x'
                return unsolved, pathMaze
            else:
                return unsolved, []
