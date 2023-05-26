import numpy as np
def binarythreshhold(result):
    if result==0.5:
        return 1
    else:
        return 0
        
def neuron(x_inputs,wt_values,bias):
    sum1=np.dot(x_inputs,wt_values)+bias
    return binarythreshhold(sum1)     
    
def notfn(x):
    #Assign wts for input of neuron
    wts=np.array([1])
    #assign bias value
    bias=0.5
    #calculate the op of ading two numbers in array x
    return neuron(x,wts,bias)

inps=[]
n=int(input("Enter no of test cases: "))  
print("Enter 1 digit 0 or 1")
for i in range(n):
    i1=int(input(""))  
    eg1=np.array([i1])
    inps.append(eg1)
    
for ins in inps:
    print("NOT (",ins[0],") : ",notfn(ins))    
