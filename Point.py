from functools import partial

colToInt = {'a' : 1, 
            'b' : 2, 
            'c' : 3, 
            'd' : 4, 
            'e' : 5, 
            'f' : 6, 
            'g' : 7, 
            'h' : 8
}

def getKey(dictionary: dict, value):     #functie voor het kijken welke key een value heeft in een dictionary ("A": range(x, y, z) etc, kijken of een getal in die range in de key valt)
    items = dictionary.items()
    for x in items:
        if value == x[1]:
            return x[0]


class Point:
    def __init__(self, x:int=0, y:int=0):
        self.x = int(x)
        self.y = int(y)
    
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)

    def __subtract__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        return Point(x, y)

    def __eq__(self, other):
        return (self.x == other.x) and (self.y == other.y)

    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)

    def isLegal(self):
        return (1 <= self.x <= 8) and (1 <= self.y <= 8)


def asSquare(pos: Point):
    return "{0}{1}".format(getKey(colToInt, pos.x), pos.y)
