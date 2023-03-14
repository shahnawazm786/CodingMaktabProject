#Loop construct
#print the hello!!! World
x=1 # intialization step
while x<=15:
    print('Hello!!! World')
    x=x+1
# example find all the odd number from 1 to 100
print("Odd number - one way")
odd=1
while odd<=100:
    print(odd,end='\t')
    odd=odd+2

print("\nOdd number - second way")
odd=1
while odd<=100:
    if odd%2!=0:
        print(odd,end='\t')
    odd=odd+1

