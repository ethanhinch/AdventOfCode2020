#Take inputs from file and store them
def getInputs():
    inputs = []
    f = open("day2.txt", "r")
    for x in f: inputs.append(x)
    return inputs
#Convert the input strings into usable form:
#   Integer lower and upper bounds, the restricted letter and the password
def parse(string):
    sections = string.split(': ')
    rule = sections[0].split(' ')
    bounds = rule[0].split('-')
    bounds[0] = int(bounds[0])
    bounds[1] = int(bounds[1])
    return [bounds[0], bounds[1], rule[1], sections[1]]
#Count the frequency of the letter in the string
def countFrequency(letter, string):
    count = 0
    for i in string:
        if(i == letter):
            count += 1
    return count
#Initialise
inputs = getInputs()
correct = 0
#Process each input and determine if rule is broken or not
for i in range(0, len(inputs)):
    parts = parse(inputs[i])
    count = countFrequency(parts[2], parts[3])
    if(count >= parts[0] and count <= parts[1]):
        correct += 1

print(correct)