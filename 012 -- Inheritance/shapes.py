class shape:
    def __init__(self, name, area):
        self.name = name
        self.area = area
        
    def calcArea(self):
        return self.area
    
class square(shape):
    def __init__(self, sideLength):
        super().__init__("Square", 0)
        self.sideLength = sideLength

    def calcArea(self):
        return self.sideLength * self.sideLength
    
mySquare = square(2)
print (mySquare.name + ", Area: " + str(mySquare.calcArea()))

class circle(shape):
    def __init__(self, radius):
        super().__init__("Circle", 0)
        self.radius = radius

    def calcArea(self):
        return 3.14 * self.radius * self.radius
        
myCircle = circle(1)
print (myCircle.name + ", Area: " + str(myCircle.calcArea()))

class halfCircle(circle):
    def __init__(self, radius):
        super().__init__(radius)
        self.name = "Half Circle"

    def calcArea(self):
        return super().calcArea() * 0.5
    
myHalfCircle = halfCircle(1)
print (myHalfCircle.name + ", Area: " + str(myHalfCircle.calcArea()))    
        
