import os
os.system('cls')
print(">>>")


from pycafee.sample import StudentDistribution
import numpy as np
x = np.array([3.335, 3.328, 3.288, 3.198, 3.254])
constant = 3.2
comparison_test = StudentDistribution()
result, conclusion = comparison_test.compare_with_constant(x, constant, conclusion='p-value', details='full')
print(result)
print(conclusion)
