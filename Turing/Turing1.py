class Developer(object):
    def __init__(self,skills):
        self.skills=skills

    def __add__(self, other):
        skills=self.skills + other.skills
        return Developer(skills)
    def __str__(self):
        return "skills"


A=Developer('NodeJS')
B=Developer('Python')

print(A+B)

def listSkills(val,list=[]):
    list.append(val)
    return  list
list1=listSkills('NodeJS')
list2=listSkills('Java',[])
list3=listSkills('ReactJS')
print('%s'%list1)
print('%s'%list2)
print('%s'%list3)
Y=[2,5J,6]
Y.sort()
print(Y)

