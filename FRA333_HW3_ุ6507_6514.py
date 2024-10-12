# file สำหรับเขียนคำตอบ
# ในกรณีที่มีการสร้าง function อื่น ๆ ให้ระบุว่า input-output คืออะไรด้วย
'''
ชื่อ_รหัส(ธนวัฒน์_6461)
1. จิรภัทร_6507
2. ชวภณ_6514
'''

# import libraries
from HW3_utils import FKHW3
import numpy as np



#=============================================<คำตอบข้อ 1>======================================================#
def endEffectorJacobianHW3(q:list[float])->list[float]:
    # Calling Forward Kinematics function using configuration space q
    Rot, Pos, Rot_end, Pos_end = FKHW3(q)

    # Declare Jacobian matrices
    J = np.empty((6, 3))

    z = [[0],[0],[1]]

    for i in range(3):
        # Calculate rotation matrix at joint i
        rot_i = np.dot(Rot[:,:,i], z).reshape(3,)

        # Calculate linear jacobian velocity matrix at joint i
        j_trans = np.cross(rot_i, Pos_end - Pos[:,i])

        # Fill in value of Jacobian matrix
        J[0][i] = j_trans[0]
        J[1][i] = j_trans[1]
        J[2][i] = j_trans[2]
        J[3][i] = rot_i[0]
        J[4][i] = rot_i[1]
        J[5][i] = rot_i[2]

    return J
#==============================================================================================================#

#=============================================<คำตอบข้อ 2>======================================================#
def checkSingularityHW3(q:list[float])->bool:
    # Initial epsilon for determining singularlity
    e = 0.001

    # Creating reduce Jacobian matrix using the first function by configuration space q
    J_red = endEffectorJacobianHW3(q)[:3, :3]

    # Calculate value to determine singularity
    val = np.linalg.det(J_red)
    if val < e:
        singularity = True
    else:
        singularity = False

    return singularity
#==============================================================================================================#

#=============================================<คำตอบข้อ 3>======================================================#
def computeEffortHW3(q:list[float], w:list[float])->list[float]:
    # Creating reduce Jacobian matrix using the first function by configuration space q
    J_red = endEffectorJacobianHW3(q)[:3, :3]

    # Reduced wrench for linear force
    w_force = np.array(w).reshape(6,1)[3:, :]

    # Calculate effort from the joint
    J_trans = np.transpose(J_red)
    tau = np.dot(J_trans, w_force)

    return tau
#==============================================================================================================#