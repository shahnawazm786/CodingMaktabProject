def show_method(*para1):
    print(para1)

def show_method1(para): #static parameter
    print(para)

def add(*val): #dynamic parameter
    total=0
    for a in val:
        total=total+a
    return total
print(add(10))
print(add(10,20))
print(add(10,20,30,40,50,60))

show_method('Java')
show_method('Java','Python')
show_method('Java','Python','Oracle')




show_method1('Unix')
#show_method1('Windows','Linux')

