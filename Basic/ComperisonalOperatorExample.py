#Operator => >,<,>=,<=, ==, !=
# These above operator not only return True or False
# The use of this operator is to compare value (number,string,date any thing)
res= 100 > 200 # left value compares the right value
print(res) #False
res=100<200
print(res) # True (left value is less to right value)

res=100 == 200
print(res) # False left value is not equal to right value

# >= => combination of > and ==
res= 100>=200
print(res) #False  => 100>200 or 100==200 (False or False) => False
res=100<=200
print(res) # True => 100<200 or 100==200 (True or False) => True
res = 100 !=200
print(res) #True

