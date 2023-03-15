d={100:"Python"}
print(type(d))
print(d)
d1=dict()
print(type(d1))

d2={
    101:"John",
    102:"Merry",
    103:"Raj",
    104:"Sohan",
    }
print(d2)
print(d2.keys())
print(d2.values())
print(d2.items())
print(d2.get(101))
print(d2[101])
d2[105]="Rahman"
print(d2)
d2[102]="Merry Jones"
print(d2)
d2.pop(102)
print(d2)
d2.popitem()
print(d2)
d2.clear()
print(d2)