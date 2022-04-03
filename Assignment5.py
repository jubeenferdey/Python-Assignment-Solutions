class Rectangle():
    def __init__(self, l,b):
        self.length = l
        self.breadth = b

    def area(self):
        print("The Area of the Rectangle is: ",self.length * self.breadth)

myRectangle = Rectangle(8,8)
myRectangle.area()
