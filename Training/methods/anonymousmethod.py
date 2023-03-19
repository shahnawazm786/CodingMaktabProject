square=lambda x: x*x

print(square(5))

add=lambda x,y: x+y
print(add(100,200))

compare=lambda x,y: x if x>y else y
print(compare(200,500))

def cube(para):
    return para*para*para
val=zip([10,5,3,4,5],[1,2,3,4],[1,2])
#print(zip)
print(list(val))

name = [ "Manjeet","Nikhil", "Shambhavi", "Astha" ]
roll_no = [ 4, 1, 3, 2 ]
val1=zip(roll_no,name)
print(set(val1))

players = ["Sachin", "Sehwag", "Gambhir", "Dravid", "Raina"]
# initializing their scores
scores = [100, 15, 17, 28, 43]

# printing players and scores.
for pl, sc in zip(players, scores):
    print("Player :  %s     Score : %d" % (pl, sc))

'''
map() function returns a map object(which is an iterator) of the 
results after applying the given function to each item of a given iterable (list, tuple etc.)
'''
# map(fun, iter)
def addition(n):
    return n + n


# We double all numbers using map()
numbers = (1, 2, 3, 4)
result = map(addition, numbers)
print(list(result))

# Double all numbers using map and lambda

numbers = (1, 2, 3, 4)
result = map(lambda x: x + x, numbers)
print(list(result))

numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]

result = map(lambda x, y: x + y, numbers1, numbers2)
print(list(result))


