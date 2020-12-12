#Take inputs from file and store them
def getInputs():
    inputs = []
    f = open("day2.txt", "r")
    for x in f: inputs.append(x)
    return inputs
#Convert the input strings into usable form:
#   Integer positions to be tested, the restricted letter and the password
def parse(string):
    sections = string.split(': ')
    rule = sections[0].split(' ')
    bounds = rule[0].split('-')
    bounds[0] = int(bounds[0])
    bounds[1] = int(bounds[1])
    return [bounds[0], bounds[1], rule[1], sections[1]]
#Check if the letter is in each specified position
def countFrequency(array):
    count = 0
    string = array[3]
    letter = array[2]
    if(string[array[0]-1] == letter):
        count += 1
    if(string[array[1]-1] == letter):
        count += 1
    return count
#Initialise
inputs = getInputs()
correct = 0
#Process each input and determine if rule is broken or not
for i in range(0, len(inputs)):
    parts = parse(inputs[i])
    count = countFrequency(parts)
    if(count == 1):
        correct += 1

print(correct)