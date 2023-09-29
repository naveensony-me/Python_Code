import numpy as np
nums = np.array([[5.54, 3.38, 7.99],
[3.54, 4.38, 6.99],
[1.54, 2.39, 9.29]])
print("Original array:")
print(nums)
n = 5
print("\nElements of the said array greater than",n)
print(nums[nums > n])
n = 6
print("\nElements of the said array less than",n)
print(nums[nums < n])