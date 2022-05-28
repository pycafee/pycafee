import os
os.system('cls')
print(">>>")


from pycafee.sample import StudentDistribution
import numpy as np
x = np.array([3380, 3500, 3600, 3450, 3490, 3390])
constant = 3450
comparison_test = StudentDistribution()
result, conclusion = comparison_test.compare_with_constant(x, constant, which="one-side", alfa=0.01, details='full')
print(result)

print(conclusion)
