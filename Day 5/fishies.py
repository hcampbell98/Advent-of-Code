import matplotlib.pyplot as plt

class Colony:
    def __init__(self, ages):
        self.fishes = []
        self.newFish = []
        self.stepNum = 0

        for age in ages:
            self.fishes.append(LanternFish(age, self))

    def addFish(self, age):
        self.newFish.append(LanternFish(age, self))

    def step(self):
        self.stepNum += 1

        for fish in self.fishes:
            fish.update()
        self.fishes = self.fishes + self.newFish
        self.newFish = []
        
    def getLength(self):
        return len(self.fishes)

class LanternFish:
    def __init__(self, internalTimer, colony):
        self.internalTimer = internalTimer
        self.colony = colony
    
    def update(self):
        if self.internalTimer == 0:
            self.internalTimer = 6
            self.colony.addFish(8)
        else:
            self.internalTimer -= 1

input = []
with open("input.txt", "r") as f:
    input = [int(x) for x in f.read().split(",")]

colony = Colony(input)

print(f"Initial Colony: {[x.internalTimer for x in colony.fishes]}")

for i in range(0, 256):
    colony.step()
    print(f"Step {i} | Colony Size: {colony.getLength()}", end="\r")

print(colony.getLength())