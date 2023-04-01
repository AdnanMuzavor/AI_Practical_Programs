tree = {
    'A': [('B', 12), ('C', 4)],
    'B': [('D', 7), ('E', 3)],
    'C': [('F', 8), ('G', 2)],
    'E': [('H', 0)],
    'F': [('H', 0)],
    'G': [('H', 0)],
    'H': []
}

start, goal = input("Enter the start and goal state: ").split(" ")


def Best_First_Search(start, goal, tree, openl=[], closel=[]):
    if start is goal:        # => START IS GOAL NODE
        closel.append(start)
        print("F O U N D: ", closel)
        return
    if start not in closel:  # => explore node with lowest heuristic value
        print(start, " Not in Close List,  e x p l o r e")
        closel.append(start)
        neighbors = tree[start]
        for nbors in neighbors:  # => Find neighbors and apppend to open
            print(nbors, " is neighbor to ", start)
            if nbors[0][0] not in openl:
                openl.append(nbors)
        # sort to get node with lowest heuristic value
        openl.sort(key=lambda x: x[1])
        print("U P D A T E D open_list: ", openl)
        if len(openl) == 0:  # open is empty, node not found
            print("N O D E   N O T   F O U N D")
            return
        if openl[0][0] is goal:  # If found
            closel.append(openl[0][0])
            print("F O U N D: ", closel)
        else:  # Otherwsie explore node with best heuristic value
            node = openl[0]
            openl.remove(node)
            Best_First_Search(node[0], goal, tree, openl, closel)


Best_First_Search(start, goal, tree, [], [])
