import numpy as np
a=np.array([[1,2,3],[4,5,6],[7,8,9]])
result=a.flatten()
print(result)
new=result[::-1]
print(new)
arr1=new.reshape(3,3)
print(arr1)

