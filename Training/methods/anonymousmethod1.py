def sum(para):
    return para+10
print(sum(10))

prt=lambda :"Hello!!! World"
print(prt)
print(prt())

def cube(x):
    return x**3

print(cube(3))
cub=lambda para: para**3
print(cub)
print(type(cub))
print(cub(4))

def greater(val1,val2):
    if val1>val2:
        return val1
    else:
        return  val2

print(greater(100,300))
print(greater(500,300))

grt=lambda x,y : x if x>y else y
print(grt(300,5))


