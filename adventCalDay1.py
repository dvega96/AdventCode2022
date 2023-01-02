firstVal = 0
secondVal = 0
thirdVal = 0
currentVal = 0
file = open("DayOneTest.txt")

for line in file:
    if line == '\n':
        if currentVal > firstVal:
            thirdVal = secondVal
            secondVal = firstVal
            firstVal = currentVal
        elif currentVal > secondVal:
            thirdVal = secondVal
            secondVal = currentVal
        elif currentVal > thirdVal:
            thirdVal = currentVal
        currentVal = 0
    else:
        currentVal += int(line)
print(firstVal + secondVal + thirdVal)
