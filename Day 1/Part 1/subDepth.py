input = []

with open("input.txt", "r") as f:
    for line in f:
        input.append(int(line))

prevDepth = None
increaseCounter = 0

for depth in input:
    if prevDepth is not None and depth > prevDepth:
        increaseCounter += 1
    prevDepth = depth

print(f"Times increased: {increaseCounter}")