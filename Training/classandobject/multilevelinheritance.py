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

class Reynolds(Link):
    def __init__(self):
        print('I am Reynolds')
    def write(self):
        print('Writing crispy')


