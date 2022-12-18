a=[1,2,3,4]
b=[sum(a[0:x+1]) for x in range(0,len(a))]
print(b)

z=set('abc')
z.add('san')
z.update(set(['p','q']))
print(z)

print(2**(3**2),(2**3)**2,(2**3)**3)
