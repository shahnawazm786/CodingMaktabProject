x=input('Enter any value')
y=input('Enter another value')
tot=0
try:
    print(x+y)
except(TypeError):
    print('Excpetion raised')
    tot=int(x)+int(y)
    print(tot)
finally:
    del(x)
    del(y)
    print('deleted the x and y variable')

try:
    print(x)
except(NameError):
    print('x is not visible')
try:
    print(y)
except:
    print('y is already deleted')
else:
    print('Else part of except')
