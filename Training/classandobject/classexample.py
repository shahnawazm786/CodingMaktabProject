class Empl():
    pass

c=Empl()

class camera():
    #class variables
    # class object varaibles
    x=10

    def __init__(self, y1, z1): #constructor
        self.y = y1
        self.z = z1

    def showxyz(self): # object method
        print(self.x)
        print(self.y)
        print(self.z)


#print(camera.x)


dslr=camera(20,40)
print(dslr.x)
print(dslr.y)
print(dslr.z)
dslr.showxyz()
