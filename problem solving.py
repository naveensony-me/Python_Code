import numpy as np
def solve(arr):
    count = 0
    for val in arr:
        if val == 0:
            count += 1
    ans = []
    for i in range(count):
        ans.append(0)
    for val in arr:
        if val != 0:
            ans.append(val)
    print(np.array(ans))
GroupA=np.array([15,0,17,0,18,0,3,11,18,20])
GroupB=np.array([9,10,4,0,8,12,0,0,18,17])
GroupC=np.array([16,6,2,10,0,0,0,11,9,5])

solve(GroupA)
solve(GroupB)
solve(GroupC)