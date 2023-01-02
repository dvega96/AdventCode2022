file = open("DayTwoTest.txt")
#file = open("test.txt")
playerOne = ""
playerTwo = ""
score = 0

def win(p1, sc):
    if p1 == "A":
        sc = 8
    elif p1 == "B":
        sc = 9
    elif p1 == "C":
        sc = 7
    return sc
    
def draw(p1, sc):
    if p1 == "A":
        sc = 4
    elif p1 == "B":
        sc = 5
    elif p1 == "C":
        sc = 6
    return sc
    
def lose(p1, sc):
    if p1 == "A":
        sc = 3
    elif p1 == "B":
        sc = 1
    elif p1 == "C":
        sc = 2
    return sc
    
for line in file:
    playerOne = line.split()[0]
    playerTwo = line.split()[1]
    if playerTwo == "X":
        score += lose(playerOne, score)
    elif playerTwo == "Y":
        score += draw(playerOne, score)
    elif playerTwo == "Z":
        score += win(playerOne, score)
print(score)