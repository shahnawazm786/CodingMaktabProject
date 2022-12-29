# Tuple is also a collection of python
# Tuple data can't be changed - readonly
# Tuple is faster than the List
# () - Tuple
# at least ',' comma
t=() #tuple
print(type(t))
t=(10) #int
print(type(t))
t=(10,30)# tuple
print(type(t))
t1=(100,)
print(type(t1))
#t1.append(10)
#t1.pop()
t2=(100,200,300,400)
print(t2)
print(t2[1])
t3=t2
print(type(t3))
print(t3)
t2=(100,200,300,400,500)
print(t2)
print(t3)
#tuple can have tuple inside
t4=(10,20,30,(1,1,3,2))
print(t4)
print(type(t4[3]))
print(t4[3][0])
#tuple can have list as well
t5=(10,20,['KAZ','codingmaktab'],17J)
print(t5)
#t5[0]=35 # exceptions
print(t5)
t5[2][0]='KAZONLINE'
print(t5)
t5[2]=['python','language']
print(t5)
