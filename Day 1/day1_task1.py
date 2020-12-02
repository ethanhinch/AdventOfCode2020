#Get input from file
input = []
f = open("day1.txt", "r")
for x in f: input.append(int(x))
#Sort
input.sort()
#Set iterators
i = 0
j = len(input) - 1
#Loop until found
while(True):
    #Set numbers
    k = input[i]
    l = input[j]
    #If i becomes higher than j, there is no solution
    if(i >= j):
        print("No solution.")
        break
    #If solution found, display and end. Otherwise, adjust an iterator
    if(k + l == 2020):
        print(k, "+", l, "=", k+l)
        print(k, "x", l, "=", k*l)
        break
    elif(k + l > 2020):
        j -= 1
    else:
        i += 1

