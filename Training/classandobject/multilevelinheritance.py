class Pen:
    def __init__(self):
        print('I am pen class')
    def write(self):
        print('Normal writing')

class Link(Pen):
    def __init__(self):
        print('I am link class')
    def write(self):
        print('Writing smooth')
    def height(self):
        print('height is normal')

class Reynolds(Link):
    def __init__(self):
        print('I am Reynolds')
    def write(self):
        print('Writing crispy')
    def color(self):
        print('bottom is white and up is blue')

r=Reynolds()
r.color()
r.height()
r.write()
l=Link()
l.write()
p=Pen()
p.write()

