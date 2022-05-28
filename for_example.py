import os
os.system('cls')
print(">>>")





from pycafee.normalitycheck import AbdiMolin
import numpy as np
x = np.array([0.8, 1, 1.1, 1.15, 1.15, 1.2, 1.2, 1.2, 1.2, 1.6, 1.8, 2, 2.2, 3, 5, 8.2, 8.4, 8.6, 9])
abdimolin_test = AbdiMolin()
result, conc = abdimolin_test.fit(x, details="full")
print(result)
# AbdiMolinResult(Statistic=0.307, Critical=0.196, p_value=None, Alpha=0.05)
print(conc)

# Since the critical value (0.196) < statistic (0.307), we HAVE evidence to reject the hypothesis of data normality, according to the AbdiMolin test at a 95.0% of confidence level.
