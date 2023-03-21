class Animal:
    age=100
    def __init__(self):
        print('Animal class')
        self.age=500
        print(self.age) #object variable
        print(Animal.age) #class variable
    def who_am_i(self):
        print('I am from Animal')

    def tanga(self):
        print('Tanga')

class Car:
    def __init__(self):
        print('Car Class')
    def who_am_i(self):
        print('I am from Car')
    def wheel(self):
        print('I have wheel')

class Baghi(Animal,Car):
    def __init__(self):
        print('Baghi Class')
    def who_am_i(self):
        print('I am from Baghi')

b=Baghi()
b.who_am_i()
b.wheel()
b.tanga()
print(b.age)

print('Animal Object')
a=Animal()
print(Animal.age)
print(a.age)




