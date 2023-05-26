# -*- coding: utf-8 -*-
"""
Created on Wed May 24 10:44:51 2023

@author: compsepm14
"""

import numpy as np
def binarythreshhold(result):
    if result<=0.5:
        return 0
    else:
        return 1
        
def neuron(x_inputs,wt_values,bias):
    sum1=np.dot(x_inputs,wt_values)+bias
    return binarythreshhold(sum1)     
    
def orfn(x):
    #Assign wts for input of neuron
    wts=np.array([1,1])
    #assign bias value
    bias=0.5
    #calculate the op of ading two numbers in array x
    return neuron(x,wts,bias)

inps=[]
n=int(input("Enter no of test cases: "))  
print("Enter 2 digits 0 or 1")
for i in range(n):
    i1=int(input(""))  
    i2=int(input(""))  
    eg1=np.array([i1,i2])
    inps.append(eg1)
    
for ins in inps:
    print("OR (",ins[0]," , ",ins[1],") : ",orfn(ins))    