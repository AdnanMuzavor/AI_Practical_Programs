graph = [
        ['A', 'H', 7, 0],
        ['A', 'B', 1, 3],
        ['A', 'C', 2, 4],
        ['B', 'D', 4, 2],
        ['B', 'E', 6, 6],
        ['C', 'F', 3, 3],
        ['C', 'G', 2, 1],
        ['D', 'E', 7, 6],
        ['D', 'H', 5, 0],
        ['F', 'H', 1, 0],
        ['G', 'H', 2, 0],
]

nodes = set([])  # Set so that it has unique values only
for edges in graph:
    nodes.add(edges[0])
    nodes.add(edges[1])

print("Nodes in graph are: ", nodes)

# Init the requirements
cost = dict()
path = dict()
openl = set()
closel = set()
for node in nodes:
    cost[node] = 10000
    path[node] = ''

start, goal = input("Enter the start and goal node: ").split(" ")  # Input

cost[start] = 0  # Init wrt to start inputed
print(cost)
path[start] = start
openl.add(start)


def AStar(start, goal, openl, closel, cost):

    if start in openl:
        openl.remove(start)
        closel.add(start)  # Explore the start as added to close with cost
    for edges in graph:

        if edges[0] == start:  # Find edges from start to a node
            from_node = edges[0]
            to_node = edges[1]
            print("found edge : ", from_node, " -> ", to_node)
            # If current cost to reach to_node is lesser then existing cost
            NEW_COST = cost[from_node]+edges[2]+edges[3]
            OLD_COST = cost[to_node]

            print(NEW_COST, OLD_COST)
            if NEW_COST < OLD_COST:
                print("found that path to: ", to_node, " via ", from_node, " is shorter with cost: ",
                      cost[from_node]+edges[2]+edges[3], " which is < ", cost[to_node])
                cost[to_node] = NEW_COST
                path[edges[1]] = path[from_node]+" - > "+to_node

    cost[start] = 10000  # Prevent start from getting selected again
    smallest = min(cost, key=cost.get)

    openl.add(smallest)
    if smallest not in closel:
        AStar(smallest, goal, openl, closel, cost)


AStar(start, goal, openl, closel, cost)
print("Path is: ", path[goal])
