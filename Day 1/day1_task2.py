#Get input from file
input = []
f = open("day1.txt", "r")
for x in f: input.append(int(x))
#Sort
input.sort()
#Finds two numbers from a list that match a third to sum to 2020
def findAddition(input, value):
    #Set iterators
    i = 0
    j = len(input) - 1
    #Loop unitl found
    while(True):
        #Set numbers
        k = input[i]
        l = input[j]
        #If no solution, end
        if(i >= j): return False
        #If solution found, return solution
        #If no solution, adjust iterator
        if(k + l == value): return [k, l]
        elif(k + l > value): j -= 1
        else: i += 1
#For each entry in the input, find two other numbers from the input that when
#added together, equal 2020         
for i in range(0, len(input)):
    #Create copy of the input without the current number in
    newInput = input.copy()
    currentVal = newInput[i]
    newInput.pop(i)
    #Find numbers using function
    result = findAddition(newInput, 2020 - input[i])
    #If answer found, display it
    if(result != False):
        print(input[i], "+", result[0],  "+", result[1],  "=", input[i] + result[0] + result[1])
        print(input[i], "x", result[0],  "x", result[1],  "=", input[i] * result[0] * result[1])
        break
    #If no answer, say that
    if(i == len(input)): print('No solution');