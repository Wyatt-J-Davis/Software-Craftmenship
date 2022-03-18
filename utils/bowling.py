class Bowler:
    def __init__(self):
        self.__throws = ""
        self.__score = 0
        
    def ScoreRolls(self, scoreSheet):
        self.__convertScoreSheet(scoreSheet) 
        return self.__calculateSetScores()
    
    def __convertScoreSheet(self, scoreSheet):
        self.__throws = scoreSheet.replace(" ","")

    def __calculateSetScores(self):
        for index,throw in enumerate(self.__throws):
            match throw:
               case 'X':
                   self.__calculateStrikeScore(index)
               case '/':
                    self.__calculateSpareScore(index)
               case '-':
                   self.__score += 0
               case _:
                   self.__score += int(throw)
        return self.__score
    
    def __calculateStrikeScore(self, index):
        notLastSets = index <= (len(self.__throws) - 3)
        if(notLastSets and (self.__throws[index + 2] != '/') ):
            self.__score += 10 + self.__rollValue(self.__throws[index + 1]) +  self.__rollValue(self.__throws[index + 2])
        elif(notLastSets):
            self.__score += 20

    def __calculateSpareScore(self, index):
        if(index < len(self.__throws) - 2):
            self.__score += 10 - int(self.__throws[index - 1]) + self.__rollValue(self.__throws[index + 1])
        else:
            self.__score += 10 - int(self.__throws[index - 1])
        
    def __rollValue(self, roll):
        match roll:
               case 'X':
                   return 10
               case '-':
                   return 0
               case _:
                   return int(roll)