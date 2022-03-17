from utils.bowling import Bowler

def TestStrikes():
    TestBowler = Bowler()
    result = TestBowler.ScoreRolls("X X X X X X X X X X X X")
    print(result)
    assert result == 300

def TestNineandMiss():
    TestBowler = Bowler()
    result = TestBowler.ScoreRolls("9- 9- 9- 9- 9- 9- 9- 9- 9- 9-")
    print(result)
    assert result == 90

def TestFiveandSpare():
    TestBowler = Bowler()
    result = TestBowler.ScoreRolls("5/ 5/ 5/ 5/ 5/ 5/ 5/ 5/ 5/ 5/5")
    print(result)
    assert result == 150

TestStrikes()
TestNineandMiss()
TestFiveandSpare()