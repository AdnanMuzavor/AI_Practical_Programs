"""______ B F S______"""
def bfs(start,tree):
    if start not in tree:
        print("INVALID start node")
        return
    visited=[]
    queue=[start]
    while queue:
        node=queue.pop(0)
        if node not in visited:
            visited.append(node)
            for child_node in tree[node]:
                if child_node not in visited:
                    queue.append(child_node)
    print("BFS TRAVERSAL IS : ",visited)
    
"""______ S E A R C H______"""
def bfs_search(start,goal,tree):
    if start not in tree:
        print("INVALID start node")
        return
    visited=[]
    queue=[start]
    while queue:
        node=queue.pop(0)    
        if node not in visited:
            visited.append(node)
            if node is goal:
                  print("Node ",goal," found, the path is: ",visited)
                  return
            for child_node in tree[node]:
                if child_node not in visited:
                    queue.append(child_node)
    print("Could not find ",goal)


"""____ I N P U T_____"""             
tree={
      'A':['B','C'],
      'B':['D','E','A'],
      'C':['F','G','A','E'],
      'D':['B'],
      'E':['B','C'],
      'F':['C'],
      'G':['C']
      }
tree={}
start,goal=input("Enter the start node and goal node: ").split(" ")
bfs(start,tree) #T R A V E R S A  L   
bfs_search(start, goal, tree) #S E A R C H