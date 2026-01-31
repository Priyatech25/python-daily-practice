class Shape:
    def area(self):
        print("Area not defined")

class Square(Shape):
    def area(self):
        print(4 * 4)

s = Square()
s.area()
