# -*- coding: utf-8 -*-
"""
Created on Wed May 24 11:32:03 2023

@author: compsepm14
"""

import numpy as np
def binarythreshhold(result):
    if result>=0:
        return 1
    else:
        return 0

        
def neuron(x_inputs,wt_values,bias):
    sum1=np.dot(x_inputs,wt_values)+bias
    return binarythreshhold(sum1)     
    
def xorfn(x):
    #Assign wts for input of each of 3 neurons
    wts_gt1=np.array([-1,-1])
    wts_gt2=np.array([-1,-1])
    wts_gt3=np.array([1,-1])
    
    #assign bias value for each og gates
    bias1=1.5
    bias2=0.5
    bias3=-0.5
    
    #Obtain reslt for gate1
    gate1_op=neuron(x,wts_gt1,bias1)
    
    #Obtain reslt for gate2
    gate2_op=neuron(x,wts_gt2,bias2)
    
    #pass gate1 and gate2 op as input to gate3
    gate_3_input=np.array([gate1_op,gate2_op])
    return neuron(gate_3_input,wts_gt3,bias3)

inps=[]
n=int(input("Enter no of test cases: "))  
print("Enter 2 digits 0 or 1")
for i in range(n):
    i1=int(input(""))  
    i2=int(input(""))  
    eg1=np.array([i1,i2])
    inps.append(eg1)
    
for ins in inps:
    print("XOR (",ins[0]," , ",ins[1],") : ",xorfn(ins))    