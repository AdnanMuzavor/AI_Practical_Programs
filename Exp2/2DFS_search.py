visited=set()
result=[]
found=False
def dfs_search(tree,node,goal):
    if node not in visited:
        result.append(node)
        visited.add(node)
        if goal in visited:
                    global found
                    found=True
                    return
        for adjnode in tree[node]:
                    if adjnode not in visited:
                        dfs_search(tree,adjnode,goal)
tree = {

    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []

}
start, goal = input("Enter start and goal state: ").split(" ")
dfs_search(tree,start,goal)
if found:
     print("Node found , path is: ",result)
else:
     print("Goal node not found")     