for x in range(1,11):
    print(x)
str="i am learning python programming"
vowel_count=0
for s in str:
    if(s=='a' or s=='i' or s=='e' or s=='o' or s=='u'):
        vowel_count=vowel_count+1

print(f"Vowel count is ->{vowel_count}")

#nested
print("-- Pattern Programming --")
for i in range(1,5):
    for j in range(1,5):
        print(j,end=' ')
    print()

for i in range(1,5):
    for j in range(1,i+1):
        print(j,end=' ')
    print()

for i in range(1,5):
    for j in range(1,i+1):
        print(i,end=' ')
    print()
