#Missing Roll Number
#Roll numbers should be from 1 to N.
#One roll number is missing.
#Find the missing roll number without sorting.
#Example:
#1 2 3 5 6
#Output:
#4

n=[1,2,3,5,6]
for i in range(1,n[-1]+1):
    if i not in n:
        print(i)

