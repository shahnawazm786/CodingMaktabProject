try:
    print(100/1)
except(ZeroDivisionError):
    print('Name error exception')
else:
    print('Excpetion not raised here')
    print(100/2)
finally:
    print('finally block')