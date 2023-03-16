#slicing value from the list
#[start:end:skip/jump]
l=[10,20,30,40,50]
print(len(l))
print(l[0])
print(l[0:2]) # 2-1 #index 1
#end-1
print(l[0:4])
print(l[0:])
print(l[1:3])
#jump
print(l[0:5:2])
# 0
# 0+2 # index ->2
# 2+2 # index ->4
print(l[0:5:4])
print(l[0::3])
#reverse
print(l[::-1])
m=l #swallow copy
n=l.copy() # deep copy
print(m)
print(n)
l.append(60)
print(l)
print(m)
print(n)


