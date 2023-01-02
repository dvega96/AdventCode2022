file = open("DayTwoTest.txt")
#file = open("test.txt")
playerOne = ""
playerTwo = ""
score = 0

# X = Rock
# Y = Paper
# Z = Scissors

def rock(p1, sc):
    if p1 == "A":
        sc = 4
    elif p1 == "B":
        sc = 1
    elif p1 == "C":
        sc = 7
    return sc
    
def paper(p1, sc):
    if p1 == "A":
        sc = 8
    elif p1 == "B":
        sc = 5
    elif p1 == "C":
        sc = 2
    return sc
    
def scissors(p1, sc):
    if p1 == "A":
        sc = 3
    elif p1 == "B":
        sc = 9
    elif p1 == "C":
        sc = 6
    return sc
    
for line in file:
    playerOne = line.split()[0]
    playerTwo = line.split()[1]
    if playerTwo == "X":
        score += rock(playerOne, score)
    elif playerTwo == "Y":
        score += paper(playerOne, score)
    elif playerTwo == "Z":
        score += scissors(playerOne, score)
    
    '''if playerTwo == "X":
        print ("rock")
    elif playerTwo == "Y":
        print ("paper")
    elif playerTwo == "Z":
        print ("Scissors")'''
        
print(score)