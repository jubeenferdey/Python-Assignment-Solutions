class Circle():
    def __init__(self, r):
        self.radius = r

    def area(self):
        print("The Area of the Circle is: ",self.radius**2*3.14)

NewCircle = Circle(8)
NewCircle.area()
