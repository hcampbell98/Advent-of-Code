report = []

with open("input.txt", "r") as f:
    report = f.readlines()

results = [0,0,0,0,0,0,0,0,0,0,0,0]
for line in report:
    for x, char in enumerate(line.strip()):
        asInt = int(char)
        results[x] = results[x] + asInt

gammaRate = ""
for result in results:
    gammaRate = gammaRate + "1" if result > len(report)/2 else gammaRate + "0"

epsilonRate = ""
for result in results:
    epsilonRate = epsilonRate + "0" if result > len(report)/2 else epsilonRate + "1"


print(int(gammaRate, 2) * int(epsilonRate, 2))
