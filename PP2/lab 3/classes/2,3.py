class Square:
    def __init__(self, length ):
        self.length  = length

    def area (self):
        print(self.length * self.length == 0)  

class Shape(Square):
    def __init__(self, length = 0 ):
        self.length  = length
    
    def area (self) :
        print(self.length * self.length) 

p = Shape(4)
p.area()
# 3 task
class Rectangle(Shape):

    def __init__(self, length,  width):
        self.length = length
        self.width = width

    def area (self):
        print( self.length  * self.width)  

# -----------------------------------

p = Rectangle(6,4)
p.area()