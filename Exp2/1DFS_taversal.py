def dfs(start,tree):
    visited = []
    stack = [start]
    while stack:
        node = stack.pop()
        visited.append(node)
        
        for adjnode in tree[node]:
            
            if adjnode not in visited:
                  stack.append(adjnode)
    print("DFS traversal is: ", visited)


"""____ I N P U T_____"""
# tree = {
#     'A': ['B', 'C'],
#     'B': ['D', 'E', 'A'],
#     'C': ['F', 'G', 'A', 'E'],
#     'D': ['B'],
#     'E': ['B', 'C'],
#     'F': ['C'],
#     'G': ['C']
# }

tree={
      
      'A':['B','C'],
      'B':['D','E'],
      'C':['F','G'],
      'D':[],
      'E':[],
      'F':[],
      'G':[]
      
      }
start = input("Enter the start node ")
dfs(start, tree)  # T R A V E R S A  L
