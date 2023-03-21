'''
def add(para):
    return para

def add(para,para1):
    return para+para1


print(add(10,20))
print(add(20))
'''
class poly:
    def __init__(self):
        pass
    def add(self,*para):
        tot=0
        for i in para:
            tot=tot+i
        return tot

p=poly()
print(p.add(20,30))
print(p.add(10,20,30,40))
