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

'''
The reduce(fun,seq) function is used to apply a particular function passed in 
its argument to all of the list elements mentioned in the sequence passed along.This function is 
defined in “functools” module.

Working :  

At first step, first two elements of sequence are picked and the result is obtained.
Next step is to apply the same function to the previously attained result and the number just 
succeeding the second element and the result is again stored.
This process continues till no more elements are left in the container.
The final returned result is returned and printed on console.

'''

import functools

# initializing list
lis = [1, 3, 5, 6, 2]

# using reduce to compute sum of list
print("The sum of the list elements is : ", end="")
print(functools.reduce(lambda a, b: a + b, lis))

# using reduce to compute maximum element from list
print("The maximum element of the list is : ", end="")
print(functools.reduce(lambda a, b: a if a > b else b, lis))

# importing functools for reduce()
import functools

# importing operator for operator functions
import operator

# initializing list
lis = [1, 3, 5, 6, 2]

# using reduce to compute sum of list
# using operator functions
print("The sum of the list elements is : ", end="")
print(functools.reduce(operator.add, lis))

# using reduce to compute product
# using operator functions
print("The product of list elements is : ", end="")
print(functools.reduce(operator.mul, lis))

# using reduce to concatenate string
print("The concatenated product is : ", end="")
print(functools.reduce(operator.add, ["python", "for", "students"]))

'''
reduce() vs accumulate() 
------------------------
Both reduce() and accumulate() can be used to calculate the summation of a sequence elements. 
But there are differences in the implementation aspects in both of these.  

reduce() is defined in “functools” module, accumulate() in “itertools” module.
reduce() stores the intermediate result and only returns the final summation value. 
Whereas, accumulate() returns a iterator containing the intermediate results. 
The last number of the iterator returned is summation value of the list.
reduce(fun, seq) takes function as 1st and sequence as 2nd argument. 
In contrast accumulate(seq, fun) takes sequence as 1st argument and function as 2nd argument.
'''


