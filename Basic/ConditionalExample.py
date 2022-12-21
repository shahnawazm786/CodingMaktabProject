# conditional operator - if - else
sal=5000
#conditional == 5000
if(sal==5000): #condition is True
    print('He is earning 5000 salary')
print('it is executed after if')

# An employee is getting 5000 or not
sal=6000
if sal==5000: # operator return False after evaluation => else is active
    print('He is getting 5000')
else:
    print('He is not getting 5000')

# An employee is getting 5000 or less or greater
sal=70000
if sal==5000: # False
    print('He is getting 5000 salary')
elif sal>5000:#True
    print('He is getting more than 5000 salary')
else:
    print('He is getting less than 5000 salary')