from utils.bowling import BowlingScorer

def TestStrikes():
    TestBowlingScorer = BowlingScorer()
    result = TestBowlingScorer.scoreRolls("X X X X X X X X X X X X")
    print(result)
    assert result == 300

def TestNineandMiss():
    TestBowlingScorer = BowlingScorer()
    result = TestBowlingScorer.scoreRolls("9- 9- 9- 9- 9- 9- 9- 9- 9- 9-")
    print(result)
    assert result == 90

def TestFiveandSpare():
    TestBowlingScorer = BowlingScorer()
    result = TestBowlingScorer.scoreRolls("5/ 5/ 5/ 5/ 5/ 5/ 5/ 5/ 5/ 5/5")
    print(result)
    assert result == 150

TestStrikes()
TestNineandMiss()
TestFiveandSpare()
