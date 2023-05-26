
#Capacity Of j1 and j2
x=int(input("Enter capacity of j1: "))
y=int(input("Enter capacity of j2: "))
z=int(input("Enter capacity of j3: "))

#What fnal state you want
goala=int(input("Enter final state of j1: "))
goalb=int(input("Enter final state of j2: "))
goalc=int(input("Enter final state of j3: "))


initial_state=(8,0,0) #Init_state
visited={}            #keep track of visisted states
path=[]               #path that leadf to soln

def wjp(state):
    #get curent states
    #print("Current state: ",state)
    a=state[0]
    b=state[1]
    c=state[2]
    #check if the goal is reached
    if a==goala and b==goalb:
        path.append(state);
        return True;
    #Check if this state was generated
    if state in visited:
        #print("Repeated state")
        return False
        
    #Else mark it visited
    visited[state]=1

    #TRy 4 cases wrt to each jug

   #Try to pour from A to B,C
    if a>0:
        #Pour a to b case
        if a+b<=y:
            if wjp((0,a+b,c)):
                path.append(state)
                return True
        else:
            if wjp((a-(y-b),y,c)):
                path.append(state)
                return True
        #Pour a to c case
        if a+c<=z:
            if wjp((0,b,a+c)):
                path.append(state)
                return True
        else:
            if wjp((a-(z-c),b,z)):
                path.append(state)
                return True
   #Try to pour from B to A,C
    if b>0:
        #Pour a to b case
        if b+a<=x:
            if wjp((a+b,0,c)):
                path.append(state)
                return True
        else:
            if wjp((x,b-(x-a),c)):
                path.append(state)
                return True
        #Pour a to c case
        if b+c<=z:
            if wjp((a,0,b+c)):
                path.append(state)
                return True
        else:
            if wjp((a,b-(z-c),z)):
                path.append(state)
                return True
   #Try to pour from C to A,B
    if c>0:
        #Pour a to b case
        if c+a<=x:
            if wjp((a+c,b,0)):
                path.append(state)
                return True
        else:
            if wjp((x,b,c-(x-a))):
                path.append(state)
                return True
        #Pour a to c case
        if c+b<=y:
            if wjp((a,b+c,0)):
                path.append(state)
                return True
        else:
            if wjp((a,y,c-(y-b))):
                path.append(state)
                return True

    return False
if wjp(initial_state):
   path.reverse()
   print("Path is: ")
   for p in path:
      print(p)   
else:
   print("No solution exists")      
      
























    