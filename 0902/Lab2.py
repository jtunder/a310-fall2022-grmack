import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return(f"({self.x}, {self.y})")
    def distanceTo(self, otherPoint):
        dx = self.x - otherPoint.x
        dy = self.y - otherPoint.y
        return math.sqrt(dx **2 + dy **2)

a = Point(1, 2)
b = Point(3, 5)

print(f"A:{a}")
print(f"B:{b}")

## Line
class Line:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2
    def length(self):
        self.point1.distanceTo(self.point2)


## Triangle
class Triangle:
    def __init__(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
    def area(self):
        a = self.p1.distanceTo(self.p2)
        b = self.p2.distanceTo(self.p3)
        c = self.p3.distanceTo(self.p1)
        s = (a + b + c) /2
        area = math.sqrt(s * (s-a) * (s-b) * (s-c))
        return area


c = Point(7, 10)
print(c)

myTriangle = Triangle(a, b, c)

print(myTriangle.area())

class Sequence:
    def __init__(self, value, rest):
        self.value = value
        self.rest = rest
    def __str__(self):
        return (f"({self.value}, {self.rest})")

ab = Sequence(1, None)
ac = Sequence(2, ab)
ad = Sequence(3, ac)

print(ad)

# (3, (2, (1, None)))


## Binary Tree
class BinaryTree:
    def __init__(self, value, leftChild, rightChild):
        self.value = value
        self.leftChild = leftChild
        self.rightChild = rightChild
    def __str__(self):
        out = ""
        if self.leftChild:
            out += str(self.leftChild) + " "
        
        out += str(self.value) + " "

        if self.rightChild:
            out += str(self.rightChild) + " "
        return out



lc = BinaryTree(5, None, None)
rc = BinaryTree(10, None, None)
myBinaryTree = BinaryTree(7, lc, rc)

print(myBinaryTree)
