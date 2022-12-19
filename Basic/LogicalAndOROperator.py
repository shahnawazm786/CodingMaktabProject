# Logical And Or and Not Operator
# AND -> all the condition is True, then result will be True
# OR -> If any conditions is True, the result will be True
# NOT -> Negations
# Usage of Logical Operator
#Logical operator used to combine Comperisional Operator
#100<200 A==A 200>100 => True
res = 100 <200 and 'A'=='A' and 200>100
print(res)
res = 100 <200 and 'A'=='A' and 200<100
print(res) # True and True and  False => False