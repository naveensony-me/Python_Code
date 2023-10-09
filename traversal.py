# Suppose there are 3 arrays of size 5 and 4th array is a size of sum of 3 array
# Now traverse all the trees in boustrophedon pattern and insert all the elements in 4th array from the begining.

a1 = [3, 4, 6, 5, 8]
a2 = [9, 1, 2, 3, 4]
a3 = [9, 8, 13, 14, 16]
a4 = [0] * 15

a1size = len(a1)
a2size = len(a2)
a3size = len(a3)
a4size = len(a4)

j = 0
temp = 0
for i in range(1, 4):
    if i == 1:
        while j < a4size - (a2size + a3size):
            a4[j] = a1[j]
            j += 1
    elif i == 2:
        temp = 1
        while j < a4size - a3size:
            a4[j] = a2[j - temp]
            j += 1
            temp += 2
    else:
        while j < a4size:
            a4[j] = a3[j - 10]
            j += 1

for i in a4:
    print(i, end=" ")
