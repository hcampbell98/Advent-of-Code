class Submarine:
    def __init__(self, x, y):
        self.horiz = x
        self.depth = y
    
    def move(self, command):
        split = command.split()

        commandWord = split[0]
        distance = int(split[1])

        if commandWord == "forward":
            self.horiz += distance
        elif commandWord == "up":
            self.depth -= distance
        elif commandWord == "down":
            self.depth += distance

    def calculate_product(self):
        return self.horiz * self.depth

with open("input.txt", "r") as f:
    commands = f.readlines()

    sub = Submarine(0, 0)

    for command in commands:
        sub.move(command)
    
    print(sub.calculate_product())
