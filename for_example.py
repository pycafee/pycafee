import os
os.system('cls')
print(">>>")



from pycafee.sample.studentdistribution import StudentDistribution
student = StudentDistribution()
result, t_student = student.get_critical_value(5, which="one-side", alfa=0.1)
print(result)
print(t_student)












#
