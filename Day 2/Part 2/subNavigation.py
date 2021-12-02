class Submarine:
    def __init__(self, x, y, z):
        self.horiz = x
        self.depth = y
        self.aim = z
    
    def move(self, command):
        split = command.split()

        commandWord = split[0]
        distance = int(split[1])

        if commandWord == "forward":
            self.horiz += distance
            self.depth += self.aim * distance
        elif commandWord == "up":
            self.aim -= distance
        elif commandWord == "down":
            self.aim += distance

    def calculate_product(self):
        return self.horiz * self.depth

sub = Submarine(0, 0, 0)
with open("input.txt", "r") as f:
    commands = f.readlines()
    for command in commands:
        sub.move(command)

print(sub.calculate_product())
