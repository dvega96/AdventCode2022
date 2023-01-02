file = open("DayFourTest.txt")
#file = open("test.txt")

a = 0
b = 0
c = 0
d = 0

count = 0

for line in file:

    #Variables for readability
    a = int(line.split(",")[0].split("-")[0])
    b = int(line.split(",")[0].split("-")[1])
    c = int(line.split(",")[1].split("-")[0])
    d = int(line.split(",")[1].split("-")[1])
    
    if (a >= c and a <= d) or (b >= c and b <= d) or (c >= a and c <= b) or (d >= a and d <= b):
       count +=1
       
print(count)