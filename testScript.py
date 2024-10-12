# file สำหรับตรวจคำตอบ
# ในกรณีที่มีการสร้าง function อื่น ๆ ให้ระบุว่า input-output คืออะไรด้วย
'''
ชื่อ_รหัส(ex: ธนวัฒน์_6461)
1. จิรภัทร_6507
2. ชวภณ_6514
'''
# import libraries
import numpy as np
from FRA333_HW3_ุ6507_6514 import endEffectorJacobianHW3 ,checkSingularityHW3 ,computeEffortHW3

# Define each joint workspaces
theta1_wrkspce = np.linspace(-np.pi, np.pi, 5) # q1
theta2_wrkspce = np.linspace(-np.pi, np.pi, 5) # q2
theta3_wrkspce = np.linspace(-np.pi, np.pi, 5) # q3

#===========================================<ตรวจคำตอบข้อ 1>====================================================#
for theta1 in theta1_wrkspce:
    for theta2 in theta2_wrkspce:
        for theta3 in theta3_wrkspce:
            # Set list q
            q = [theta1 ,theta2 ,theta3]

            # Random wrench list
            w = np.random.rand(1,6)

            # Calling function to find EndEffector Jacobian
            J_e = endEffectorJacobianHW3(q)

            # Calling function to check Singularity
            singularity = checkSingularityHW3(q)

            # Calling function to compute Effort
            tau = computeEffortHW3(q ,w)

            # Showing inputs along with outputs
            print('Singularity :' , singularity) #คำถามข้อที่ 2

            print('Q :' , q)

            print('Input Force :' , w)

            print('Jacobian Matrics :\n' , J_e ) #คำถามข้อที่ 1

            print('Joint Effort :\n' , tau) #คำถามข้อที่ 

            print('\n', 'x' * 100 , '\n' )

#==============================================================================================================#