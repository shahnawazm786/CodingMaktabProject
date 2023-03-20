def filt(val):
        if(val%3==0):
            return val

print(filt(4))
num=[2,3,4,5,6,7,8,9]
res1= filter(filt,num)
print(res1)
print(list(res1))
res2=filter(lambda x : x%3==0,num)
print(res2)
print(list(res2))
