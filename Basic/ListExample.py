# List ->
# Usage of List
# what is the age of user A
A=45 # single unit and single value
# Store and process the age of two person
Person1=60
Person2=65
# Person of age the
# Collection give me the feature to store and process the multiple value in a single unit
Age=[16,45,35,90,40]
print(Age)
# If you want to access single value from the single unit, we have to use the index
# index start with 0
print(Age[0])
#List -> when the value kept in []
# type()
print(type(Age))
Empty=[]
print(type(Empty))
Empty=[10]
print(type(Empty)) # data type
print(Empty) #  all value of Empty list
print(Empty[0]) # value lies on 0th index of Empty list
# By nature list is mutable
# Mutable value of the List is changable
Age=[16,45,35,90,40]
print(Age)
Age[1]=55
print(Age)
#Add the value 25 between 16 and 55
Age.insert(1,20)
print(Age)
# Append function is used to add value at the last of the list
Age.append(100)
print(Age)
# Remove the 90 from the list
# [16, 20, 55, 35, 90, 40, 100]
Age.remove(90)
print(Age)
Age.pop()
print(Age)






