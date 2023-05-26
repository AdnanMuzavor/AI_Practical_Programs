# -*- coding: utf-8 -*-
"""
Created on Wed May 24 10:58:04 2023

@author: compsepm14
"""

import numpy as np
def binarythreshhold(result):
    if result>=3.5:
        return 1
    else:
        return 0
        
def neuron(x_inputs,wt_values,bias):
    sum1=np.dot(x_inputs,wt_values)+bias
    return binarythreshhold(sum1)     
    
def andfn(x):
    #Assign wts for input of neuron
    wts=np.array([1,1,1])
    #assign bias value
    bias=0.5
    #calculate the op of ading two numbers in array x
    return neuron(x,wts,bias)

inps=[]
n=int(input("Enter no of test cases: "))  
print("Enter 3 digits 0 or 1")
for i in range(n):
    i1=int(input(""))  
    i2=int(input(""))  
    i3=int(input(""))  
    eg1=np.array([i1,i2,i3])
    inps.append(eg1)
    
for ins in inps:
    print("And (",ins[0]," , ",ins[1]," , ",ins[2],") : ",andfn(ins))  