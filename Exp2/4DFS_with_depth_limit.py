def Dedpth_limit_srch(tree, start, goal, depth_limit, level, path):
    print("Current level : ", level)
    if start is goal:
        print("Node found -> path is: ", path)
        return True
    else:
        print(f"EXPANDING NODE: {start} at level : {level}")
    if level == depth_limit:
        print(f"{start} is at level > DEPTH LIMIT: {depth_limit} HENCE _STOP_")
        return False
    neighbor = tree[start]
    for node in neighbor:

        """new_path=path
        new_path.append(node)"""

        # If node is found true will be returned => if so stop by returning
        # Othwise continue with opther neighbors
        path.append(node)
        if Dedpth_limit_srch(tree, node, goal, depth_limit, level+1, path):
            return True
        path.pop()
    return False


tree = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],  # B LEVEL = 1
    'C': ['F', 'G'],  # C LEVEL = 1
    'D': [],
    'E': [],
    'F': [],
    'G': []
}

start, goal, depth_limit = input(
    "Enter styart state, goal state anbd maximum depth: ").split(" ")
depth_limit = int(depth_limit)
path = [start]
if Dedpth_limit_srch(tree, start, goal, depth_limit, 0, path) is False:
    print(f"{goal} not found")
