# FRA333_HW3_6507_6514
**จาก HW3 โจทย์ให้หาค่า**
 - Jacobians Matrics
 - Singularity
 - Joint Effort

**รูปภาพของแขนกล**
![Robot_arm](pic1.png)

# Function
โดยมี 3 Function ก็คือ 
- endEffectorJacobianHW3 เป็น Fuction สำหรับการหา Jacobian Matrics จาก Joint Config ของแขนกล
- checkSingularityHW3 เป็น Fuction เพื่อเช็คว่าเกิด Singularity หรือไม่ จาก Joint Config ของแขนกล
- computeEffortHW3 เป็น Function สำหรับการหา Joint Effort จาก Joint Config และ Wrench ที่กระทำต่อ $F_e$
