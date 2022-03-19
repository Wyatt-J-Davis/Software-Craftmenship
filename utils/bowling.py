class BowlingScorer:
    def __init__(self):
        self.__rolls = ""
        
    def ScoreRolls(self, scoreSheet):
        self.__rolls = scoreSheet.replace(" ","") 
        return self.__calculateScore()

    def __calculateScore(self):
        score = 0
        for index,roll in enumerate(self.__rolls):
            match roll:
               case 'X':
                   score += self.__calculateStrikeScore(index)
               case '/':
                   score += self.__calculateSpareScore(index)
               case '-':
                   score += 0
               case _:
                   score += int(roll)
        return score
    
    def __calculateStrikeScore(self, index):
        amountToAdd = 0
        notLastTwoFrames = index <= (len(self.__rolls) - 3)
        if(notLastTwoFrames):
            nextFrameNotSpare = (self.__rolls[index + 2] != '/')
            if(nextFrameNotSpare):
                amountToAdd += 10
                amountToAdd += self.__rollValue(self.__rolls[index + 1])
                amountToAdd += self.__rollValue(self.__rolls[index + 2])
            else:
                amountToAdd += 20
        return amountToAdd

    def __calculateSpareScore(self, index):
        amountToAdd = 0
        notLastFrame = index < len(self.__rolls) - 2
        if(notLastFrame):
            amountToAdd += 10 
            amountToAdd -= int(self.__rolls[index - 1])
            amountToAdd += self.__rollValue(self.__rolls[index + 1])
        else:
            amountToAdd += 10
            amountToAdd -= int(self.__rolls[index - 1])
        return amountToAdd
        
    def __rollValue(self, roll):
        match roll:
               case 'X':
                   return 10
               case '-':
                   return 0
               case _:
                   return int(roll)