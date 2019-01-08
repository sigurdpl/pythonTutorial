
class Zombie:
    def __init__(self, name):
        self.name = name
        self.x = 0
        self.y = 0
    def walk(self, direction):
        if direction=='left':
            self.x = self.x - 1
        elif direction == 'right':
            self.x = self.x + 1
        elif direction == 'up':
            self.y = self.y - 1
        else:
            self.y = self.y + 1
        print(self.name + ' walking to x=' + str(self.x) + 'y=' + str(self.y))


