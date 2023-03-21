print(10+10)
print(10/10)
try:
    print(10/0) # exception occured at runtime
except:
    print('exception raised')
# when occur, control flow is disrupted when it is not handle
print('Hello!!!')

try:
    print(100/0)
except(ZeroDivisionError):
    print('Zero division error')

x=input('Enter any value')
try:
    print(x+120)
except(TypeError):
    print(int(x)+120)


