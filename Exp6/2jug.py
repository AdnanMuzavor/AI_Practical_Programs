
#Capacity Of j1 and j2
j1cap=int(input("Enter capacity of j1: "))
j2cap=int(input("Enter capacity of j2: "))

#What fnal state you want
final_j1=int(input("Enter final capacity of j1: "))
final_j2=int(input("Enter final capacity of j2: "))

#Initialise the jugs
jug1=0
jug2=0
print("Initial: [",jug1," , ",jug2," ]")
print("Final: [",final_j1," , ",final_j2," ]")
print("1 => Fill jug A completely")
print("2 => Fill jug B completely")
print("3 => Pour from jug A completely onto the ground")
print("4 => Pour from jug B completely onto the ground")
print("5 => Pour from Jug A to Jug B until it s full or A becomes empty")
print("6 => Pour from Jug B to Jug A until it s full or B becomes empty")
print("7 => Pour all water from Jug B to Jug A")
print("8 => Pour all water from Jug A to Jug B")

while jug1!=final_j1 or jug2!=final_j2:
    op=int(input("Enter the rule number: "))
    if op==1:
        jug1=j1cap
    elif op==2:
        jug2=j2cap
    elif op==3:
        jug1=0
    elif op==4:
        jug2=0
    elif op==5:
        if jug1+jug2<=j2cap:
            jug2=jug1+jug2
            jug1=0
        else:
            jug1=(jug1+jug2)-j2cap
            jug2=j2cap
    elif op==6:
        if jug1+jug2<=j1cap:
            jug1=jug1+jug2
            jug2=0
        else:
            jug2=(jug1+jug2)-j1cap
            jug1=j1cap
    elif op==7:
        jug1=jug1+jug2
        if jug1>j1cap:
            jug1=j1cap
        jug2=0
    elif op==8:
        jug2=jug1+jug2
        if jug2>j2cap:
            jug2=j2cap
        jug1=0    
    print("j1: ",jug1," j2: ",jug2)     
print("Goal Achieved")    
    