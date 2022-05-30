import os
os.system('cls')
print(">>>")




from pycafee.normalitycheck import NormalityCheck
import numpy as np
x = np.array([5.1, 4.9, 4.7, 4.6, 5.0, 5.4, 4.6, 5.0, 4.4, 4.9])
normality_test = NormalityCheck()
result, conclusion = normality_test.fit(x, test="am")
print(result)
# AbdiMolinResult(Statistic=0.154, Critical=0.261, p_value=None, Alpha=0.05)
print(conclusion)
# Data is Normal at a 95.0% of confidence level.
