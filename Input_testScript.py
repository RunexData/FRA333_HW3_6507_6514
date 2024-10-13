# import libraries
import numpy as np
from FRA333_HW3_ุ6507_6514 import endEffectorJacobianHW3 ,checkSingularityHW3 ,computeEffortHW3
#Mode Selector
print('----- Select Mode 1-5 -----')
print('Mode 1 : Jacobian')
print('Mode 2 : Singularity')
print('Mode 3 : Joint Effort')
print('Mode 4 : Jacobian & Singularity') 
print('Mode 5 : Jacobian & Singularity & Joint Effort')
mode = int(input("Mode : "))

#Mode 1
if(mode == 1):
    print('\n' + 'Mode : Jacobian' + '\n')
    print('----- Input q1, q2, q3 -----') #Input q 
    print('Value between -3.14 to 3.14')
    q1 = float(input('q1 :'))
    q2 = float(input('q2 :'))
    q3 = float(input('q3 :'))

    q = [q1 ,q2 ,q3] #Set List q
    J_e = endEffectorJacobianHW3(q) #Calling Function to calculate Jacobian

    print('Jacobian Matrics :\n' , J_e )
    print('\n', 'x' * 100 , '\n' )

#Mode 2
if(mode == 2):
    print('\n' + 'Mode : Singularity' + '\n')
    print('----- Input q1, q2, q3 -----') #Input q 
    print('Value between -3.14 to 3.14')
    q1 = float(input('q1 :'))
    q2 = float(input('q2 :'))
    q3 = float(input('q3 :'))

    q = [q1 ,q2 ,q3]
    singularity = checkSingularityHW3(q) #Calling Function to check singularity

    print('Singularity :' , singularity)
    print('\n', 'x' * 100 , '\n' )


#Mode 3
if(mode == 3):
    print('\n' + 'Mode : Joint Effort' + '\n')
    print('----- Input q1, q2, q3 -----') #Input q 
    print('Value between -3.14 to 3.14')
    q1 = float(input('q1 :'))
    q2 = float(input('q2 :'))
    q3 = float(input('q3 :'))

    print('----- Input w1, w2, w3, w4, w5, w6 -----') #Input w
    w1 = float(input('w1 :'))
    w2 = float(input('w2 :'))
    w3 = float(input('w3 :'))
    w4 = float(input('w4 :'))
    w5 = float(input('w5 :'))
    w6 = float(input('w6 :'))

    q = [q1, q2, q3] #Set list q
    w = [w1, w2, w3, w4, w5, w6] #Set list w
    tau = computeEffortHW3(q ,w) #Calling Function to calculate Joint Effort

    print('Joint Effort :\n' , tau) 
    print('\n', 'x' * 100 , '\n' )

#Mode 4
if(mode == 4):
    print('\n' + 'Mode : Jacobian & Singularity' + '\n')
    print('----- Input q1, q2, q3 -----') #Input q 
    print('Value between -3.14 to 3.14')
    q1 = float(input('q1 :'))
    q2 = float(input('q2 :'))
    q3 = float(input('q3 :'))

    q = [q1 ,q2 ,q3]
    J_e = endEffectorJacobianHW3(q)
    singularity = checkSingularityHW3(q)

    print('Jacobian Matrics :\n' , J_e )
    print('Singularity :' , singularity)
    print('\n', 'x' * 100 , '\n' )

#Mode 5
if(mode == 5):
    print('\n' + 'Mode : Jacobian & Singularity & Joint Effort' + '\n')
    print('----- Input q1, q2, q3 -----') #Input q
    print('Value between -3.14 to 3.14')
    q1 = float(input('q1 :'))
    q2 = float(input('q2 :'))
    q3 = float(input('q3 :'))
    print('\n', 'x' * 100 , '\n' )

    print('----- Input w1, w2, w3, w4, w5, w6 -----') #Input w
    w1 = float(input('w1 :'))
    w2 = float(input('w2 :'))
    w3 = float(input('w3 :'))
    w4 = float(input('w4 :'))
    w5 = float(input('w5 :'))
    w6 = float(input('w6 :'))

    q = [q1 ,q2 ,q3] #Set list q
    w = [w1, w2, w3, w4, w5, w6] #Set list w
    J_e = endEffectorJacobianHW3(q) #Calling Function to calculate Jacobian
    singularity = checkSingularityHW3(q) #Calling Function to check singularity
    tau = computeEffortHW3(q ,w) #Calling Function to calculate Joint Effort

    print('Jacobian Matrics :\n' , J_e )
    print('Singularity :' , singularity)
    print('Joint Effort :\n' , tau)
    print('\n', 'x' * 100 , '\n' )

