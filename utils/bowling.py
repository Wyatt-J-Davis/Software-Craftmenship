

class Bowler:
    def __init__(self):
        #self.__setScores = []
        self.__throws = ""
        self.__score = 0
        
    def ScoreRolls(self, scoreSheet):
        # Convert scoresheet into more convenient data structure
        self.__convertScoreSheet(scoreSheet)
        # Convert throws into scores for the sets and 
        return self.__calculateSetScores()
    
    def __convertScoreSheet(self, scoreSheet):
        self.__throws = scoreSheet.replace(" ","")

    def __calculateSetScores(self):
        for index,throw in enumerate(self.__throws):
            match throw:
            # Check if throw is strike
               case 'X':
                   self.__calculateStrikeScore(index)
            # Check if throw is spare
               case '/':
                    self.__calculateSpareScore(index)
            # Check if throw is a miss
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
            # Check if throw is strike
               case 'X':
                   return 10
            # Check if throw is a miss
               case '-':
                   return 0
               case _:
                   return int(roll)