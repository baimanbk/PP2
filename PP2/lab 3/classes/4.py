class Points():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def show(self):
        print('coordinates of the point ' + 'x = ' + str(self.x) + ' and '+ ' y = ' + str(self.y))
    def move(self):
        self.t = self.y
        self.y = self.x
        self.x = self.t
    def dist(self):
        print(abs(self.y - self.x))
p = Points(4, 7)
p.show()
p.dist()
p.move()
p.show()
p.dist()