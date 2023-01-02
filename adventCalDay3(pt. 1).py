file = open("DayThreeTest.txt")
#file = open("test.txt")

rucksackOne = ""
rucksackTwo = ""
totalValue = 0

for line in file:

    #Assign rucksackOne first half of string
    #Assign rucksackTwo second half of string
    rucksackOne = line[slice(0, len(line)//2)]
    rucksackTwo = line[slice(len(line)//2, len(line))]
    
    #loop through each character in rucksackOne 
    #and compare to each character in rucksackTwo
    for r1Char in rucksackOne:
        #find function to avoid second for loop & easy break out of loop when duplicate value found
        if rucksackTwo.find(r1Char) != -1:
            #print(r1Char + " ASCII val: " + str(ord(r1Char)))
            
            #Take ascii value and subtract by 96 if lower
            if r1Char.islower():
                totalValue += ord(r1Char) - 96
            #subtract ascii value by 38 if upper
            else:
                totalValue += ord(r1Char) - 38
            break
            
print(totalValue)
            
        
