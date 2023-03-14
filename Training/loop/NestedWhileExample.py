'''
1 1 1 1
2 2 2 2
3 3 3 3
4 4 4 4
------------
1
1 2
1 2 3
1 2 3 4
---------
1
2 2
3 3 3
4 4 4 4

'''
print("Pattern -1")
x=1
while x<=4:
    y=1
    while y<=4:
        print(x,end='')
        y=y+1
    print()
    x=x+1
print()
print("Pattern -2 ")
z=1
while z<=4:
    a=1
    while a<=z:
       print(z,end='')
       a=a+1
    z=z+1
