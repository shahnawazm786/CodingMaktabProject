def cube(val):
    return val**3

l=[2,3,4,5]
res=map(cube,l)
print(list(res))
res1= map(lambda x: x**3,l)
print(list(res1))



