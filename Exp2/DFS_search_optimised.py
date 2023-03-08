def dfs_path_optimised(tree, start, goal):
    visited = []
    stack = [[start]]
    if start == goal:
        print(start, " is the goal node ")
    while stack:
        path = stack.pop()
        node = path[-1]
        if node not in visited:
            visited.append(node)
        neighbour = tree[node]
        for i in neighbour:
            new_path = list(path)
            new_path.append(i)
            stack.append(new_path)
            if i == goal:
                return new_path


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

print("Shortest Path is : ", dfs_path_optimised(tree, start, goal))


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
