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
        print(x,end=' ')
        y=y+1
    print()
    x=x+1
print()
print("Patter -2")
l=1
while l<=4:
    m=1
    while m<=l:
        print(m,end=' ')
        m=m+1
    print()
    l=l+1
print()
print("Pattern -3 ")
z=1
while z<=4:
    a=1
    while a<=z:
       print(z,end=' ')
       a=a+1
    print()
    z=z+1

