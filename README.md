# FRA333_HW3_6507_6514
**จาก HW3 โจทย์ให้หาค่า**
 - Jacobians Matrics
 - Singularity
 - Joint Effort

**รูปภาพของแขนกล**
![Robot_arm](pic1.png)

# Function
โดยมี 3 Function ก็คือ 
- endEffectorJacobianHW3 เป็น Fuction สำหรับการหา Jacobian Matrics จาก Joint Configuration ของแขนกล
- checkSingularityHW3 เป็น Fuction เพื่อเช็คว่าเกิด Singularity หรือไม่ จาก Joint Configuration ของแขนกล
- computeEffortHW3 เป็น Function สำหรับการหา Joint Effort จาก Joint Configuration และ Wrench ที่กระทำต่อ $F_e$

# endEffectorJacobianHW3
โดยการหา Jacobian Matrics จะมีค่าที่ต้องกำหนดคือ
- Input : $q_1$, $q_2$, $q_3$ ซึ่งเป็น ค่าของ Joint Configuration ของแขนกล

และมี Ouput เป็น $J^{6x6}$ หรือก็คือ Endeffector Jacobian Matric 

