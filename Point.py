class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)

    def __subtract__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        return Point(x, y)

    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)
    
    def isLegal(self):
        return (1 <= self.x <= 8) and (1 <= self.y <= 8)