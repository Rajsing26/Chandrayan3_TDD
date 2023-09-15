# In chandrayaan3.py


class SpaceCraft:
    def __init__(self):
        # Initial position (x, y, z)
        self.position = [0, 0, 0]
        # Initial direction (N, S, E, W, U, D)
        self.direction = "N"
        self.prev = None

    def move(self, command, dir):
        if command == "b":
            if dir == "N":
                self.position[1] -= 1
            elif dir == "S":
                self.position[1] += 1
            elif dir == "E":
                self.position[0] -= 1
            elif dir == "W":
                self.position[0] += 1
            elif dir == "U":
                self.position[2] -= 1
            elif dir == "D":
                self.position[2] += 1
        elif command == "f":
            if dir == "N":
                self.position[1] += 1
            elif dir == "S":
                self.position[1] -= 1
            elif dir == "E":
                self.position[0] += 1
            elif dir == "W":
                self.position[0] -= 1
            elif dir == "U":
                self.position[2] += 1
            elif dir == "D":
                self.position[2] -= 1
        

    def turn(self, command, dir):
        if command == "r":
            if dir == "N":
                self.direction = "E"
            elif dir == "S":
                self.direction = "W"
            elif dir == "E":
                self.direction = "S"
            elif dir == "W":
                self.direction = "N"
            elif dir == "U":
                self.turn(command, self.prev)
            elif dir == "D":
                self.turn(command, self.prev)
        elif command == "l":
            if dir == "N":
                self.direction = "W"
            elif dir == "S":
                self.direction = "E"
            elif dir == "E":
                self.direction = "N"
            elif dir == "W":
                self.direction = "S"
            elif dir == "U":
                # Use previous direction
                self.turn(command, self.prev)  
            elif dir == "D":
                # calling function with previous direction values
                self.turn(command, self.prev)  
        

    def tilt(self, command, dir):
        if command == "u":
            if dir == "N":
                self.prev = "N"  # storing for turn purpose
                self.direction = "U"
            elif dir == "S":
                self.prev = "S"
                self.direction = "U"
            elif dir == "E":
                self.prev = "E"
                self.direction = "U"
            elif dir == "W":
                self.prev = "W"
                self.direction = "U"
            else:
                self.direction = "U"
        elif command == "d":
            if dir == "N":
                self.prev = "N"
                self.direction = "D"
            elif dir == "S":
                self.prev = "S"
                self.direction = "D"
            elif dir == "E":
                self.prev = "E"
                self.direction = "D"
            elif dir == "W":
                self.prev = "W"
                self.direction = "D"
            else:
                self.direction = "D"

    def command_execute(self, commands):
        for command in commands:
            if command in ("f", "b"):
                self.move(command, self.direction)
            elif command in ("l", "r"):
                self.turn(command, self.direction)
            elif command in ("u", "d"):
                self.tilt(command, self.direction)

    def getPosition(self):
        return self.position

    def getDirection(self):
        return self.direction
