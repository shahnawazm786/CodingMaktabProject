
def f(x,l=[]):
    for i in range(x):
        l.append(i*i)
    print(l)

f(2)
f(3,[3,2,1])
f(3)

print([i.lower() for i in "TURING"])
'The {} side {1} {2}'.format('bright','of','life')
