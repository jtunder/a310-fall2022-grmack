import math

############################### Point Class #############################


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def distanceTo(self, other):
        distance = math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)
        return distance


print("---------------------------Class Point---------------------------")
a = Point(3, 2)
b = Point(-1, 5)
print(f"I have two point objects: {a} and {b}")

howFar = a.distanceTo(b)
print("Distance from {a} to {b} is {howFar}")

############################### Line Class #############################


class Line(Point):
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __str__(self):
        return f"({self.p1}, {self.p2})"

    def length(self):
        return self.p2.distanceTo(self.p1)


print("---------------------------Class Line---------------------------")
a = Point(3, 2)
b = Point(-1, 7)
c = Line(a, b)
distance = c.length()
print("Length of line {c} is {distance}")

############################### Triangle Class #############################


class Triangle(Line):
    def __init__(self, p1, p2, p3):
        self.l1 = Line(p1, p2)
        self.l2 = Line(p2, p3)
        self.l3 = Line(p3, p1)

    def __str__(self):
        return "Triangle {" + str(self.l1.p1) + ", " + str(self.l2.p1) + ", " + str(self.l3.p1) + "}"

    def area(self):
        x = (self.l1.length() + self.l2.length() + self.l3.length())/2
        a = math.sqrt(x*(x - self.l1.length()) *
                      (x - self.l2.length())*(x - self.l3.length()))
        return a


print("---------------------------Class Triangle---------------------------")
a = Point(4, 5)
b = Point(2, 2)
c = Point(5, 1)
tri = Triangle(a, b, c)
A = tri.area()
print(f"Area of {tri} is {A}")

############################### Sequence Class #############################


class Sequence:
    def __init__(self, value, rest):
        self.value = value
        self.rest = rest

    def __str__(self):
        return (f"({self.value}, {self.rest})")


print("---------------------------Class Sequence---------------------------")
a = Sequence("Bob", None)
a = Sequence("Gru", a)
print(a)

############################### BinaryTree Class #############################


class BinaryTree:
    def __init__(self, value, left, right):
        (self.value, self.left, self.right) = (value, left, right)

    def show(self):
        if self.left == None:
            left = " . "
        else:
            left = self.left.show()
        if self.right == None:
            right = " . "
        else:
            right = self.right.show()

        return f"({left} {self.value} {right})"


print("---------------------------Class BinaryTree---------------------------")
a = BinaryTree(5, None, None)
print(a.show())

a = BinaryTree(1, a, None)
print(a.show())

a = BinaryTree(2, BinaryTree(4, None, a), None)
print(a.show())
