
"""____________F U NC C T I O N : P A T H____________"""
def path(op):
    print("___P A T H___:")
    print("---------------")
    for i in range(len(op)-1):
        print(op[i]," -> ",end="")
    print(op[len(op)-1])
    print("---------------")

"""_____________F U N C T I O N : D F S _____________"""
found=False
def DFS(graph,node,key,vis,op):
    vis[node]=True
    #print(f"{node} added in op")
    op.append(node)
    if node is key:
        #print(f"{key} found in the graph")
        path(op)
        global found
        found=True
       
        return
    for adjnode in graph[node]:
        if(vis[adjnode] is False):
            DFS(graph,adjnode,key,vis,op)
    op.pop()        
    #print(f"{node} popped in op")




"""____ E D G E S  AND  N O D E S____"""
n,e=[int(x) for x in input("Enter number of nodes and edges: ").split()]
graph={}
"""______________G R A P H________________"""
for i in range(e):
    n1,n2=[int(x) for x in input("Enter n1 and n2: ").split()]
    #n2 is adjacent to n1 so add it to list of nodes adjacent to n1
    if n1 not in graph:
        graph[n1]=[n2]
    else:
        graph[n1].append(n2);    
    #n1 is adjacent to n2 so add it to list of nodes adjacent to n2
    if n2 not in graph:
        graph[n2]=[n1]
    else:
        graph[n2].append(n1);      
"""_______D I S P L A Y______"""

print(graph)

"""______K E Y_____"""
key=int(input("Enter the key: "))

"""______ I N I T I A L I Z A T I O N  AND D I S P L A Y_______"""
vis=[False]*n
op=[]
DFS(graph,0,key,vis,op)
if found is not True:
    print(f"{key} could not be found in graph")    
