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
    
    def isOutside(self):
        return (self.x > 8 or self.y > 8 or self.x < 1 or self.y < 1)