input = []

with open("input.txt", "r") as f:
    for line in f:
        input.append(int(line))

lengthOfInput = len(input)
sumsOfInputs = []
for x in range(0, lengthOfInput):
    if x < lengthOfInput - 2:
        sumsOfInputs.append(input[x] + input[x+1] + input[x+2])

prevSum = None
increaseCounter = 0
for sum in sumsOfInputs:
    if prevSum is not None and sum > prevSum:
        increaseCounter += 1
    prevSum = sum

print(increaseCounter)