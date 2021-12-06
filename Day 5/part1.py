from typing import overload
import matplotlib.pyplot as plt
import numpy as np
import math

class Line:
    def __init__(self, rawInput):
        splitAroundArrow = rawInput.split(' -> ')
        self.point1 = self.getPointFromInput(splitAroundArrow[0].split(','))
        self.point2 = self.getPointFromInput(splitAroundArrow[1].split(','))
    
    def getPointFromInput(self, input):
        return (int(input[0]), int(input[1]))
    
    def getPoints(self):
        points = []

        if self.point1[0] == self.point2[0]:
            minY = min(self.point1[1], self.point2[1])
            maxY = max(self.point1[1], self.point2[1])

            minX = min(self.point1[0], self.point2[0])

            for i in range(0, maxY - minY + 1):
                points.append((minX, minY + i))
        elif self.point1[1] == self.point2[1]:
            minX = min(self.point1[0], self.point2[0])
            maxX = max(self.point1[0], self.point2[0])

            minY = min(self.point1[1], self.point2[1])

            for i in range(0, maxX - minX + 1):
                points.append((minX + i, minY))

        return points

input = []

with open('input.txt', 'r') as f:
    input = f.read().splitlines()

lines = [Line(line) for line in input]

#only check lines that are horizontal or vertical
horizontalLines = [line for line in lines if line.point1[0] == line.point2[0]]
verticalLines = [line for line in lines if line.point1[1] == line.point2[1]]


horizAndVert = horizontalLines + verticalLines
print("Number of lines:", len(horizAndVert))

grid = np.zeros((1000, 1000), dtype=int)

for line in horizAndVert:
    for point in line.getPoints():
        grid[point[0], point[1]] += 1

overlaps = 0
for row in grid:
    for cell in row:
        if cell > 1:
            overlaps += 1

print("Overlaps:", overlaps)

plt.imshow(grid, interpolation='none')
plt.show()
