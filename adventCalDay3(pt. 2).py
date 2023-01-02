file = open("DayThreeTest.txt")
#file = open("test.txt")

elfOne = ""
elfTwo = ""
x = 1
totalValue = 0

for line in file:

    if x == 1:
        elfOne = line
        x+=1
    elif x == 2:
        elfTwo = line
        x+=1
    else:
        
        #loop through each character in elfOne line
        #and compare to each character in elfTwo & elfThree lines
        for e1Char in elfOne:
            #find function to avoid second for loop 
            #& easy break out of loop when duplicate value found
            if elfTwo.find(e1Char) != -1 and line.find(e1Char) != -1:                
                #Take ascii value and subtract by 96 if lower
                if e1Char.islower():
                    totalValue += ord(e1Char) - 96
                #subtract ascii value by 38 if upper
                else:
                    totalValue += ord(e1Char) - 38
                x = 1
                break
            
print(totalValue)