#Consecutive Duplicate Detector
#Accept N integers.
#Display only those numbers that appear consecutively more than once.
#Input:
#1 2 2 3 4 4 4 5
#Output:
#2
#4

n=[1,2,2,3,4,4,4,5]
dup=[]
for i in n:
    if n. count(i)>1 and i not in dup:
        dup.append(i)
print(dup)