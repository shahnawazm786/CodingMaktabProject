class Animal:
    def __int__(self):
        print('Animal class')
    def who_am_i(self):
        print('I am from Animal')

class Car:
    def __int__(self):
        print('Car Class')
    def who_am_i(self):
        print('I am from Car')

class Baghi(Animal,Car):
    def __int__(self):
        print('Baghi Class')
    def who_am_i(self):
        print('I am from Baghi')




