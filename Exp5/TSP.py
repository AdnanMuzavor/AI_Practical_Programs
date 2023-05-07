nodes_count = int(input("Enter the number 0f cities: "))  # nodes a re cities

edges_count = int(input("Enter the number 0f connections: ")
                  )  # connection are edges

# Take connectiopns as i/p from the user
connection_list = []
print("Enter from_city, to city, cost: ")
for i in range(edges_count):
    from_city, to_city,cost = input("").split(" ")
    cost = int(cost)
    connection_list.append([from_city, to_city, cost])

# nodes_count = 4
# connection_list = [['A', 'B', 10], ['A', 'C', 20], [
#     'A', 'D', 15], ['B', 'C', 25], ['C', 'D', 30], ['B', 'D', 35]]

# Undirected graph hence reverse the edges
final_list = []
for connectionL in connection_list:
    from_node = connectionL[0]
    to_node = connectionL[1]
    cost = connectionL[2]
    final_list.append([to_node, from_node, cost])

for connectionL in final_list:
    connection_list.append(connectionL)

start = input("Enter the starting city: ")


def TSP(connection_list, current, start, visited, total_cost, nodes_count):
    print(current, start)
    if len(visited) == nodes_count:
        for connectionL in connection_list:
            if (connectionL[0] == current and connectionL[1] == start):
                total_cost = total_cost+connectionL[2]
                break

        print("Path is: ", visited, " Total cost : ", total_cost) 
        return
    selected_node = ""
    selected_cost = 100000
    # Explore path from start to other node and take the best one not visited
    for connectionL in connection_list:
        from_city = connectionL[0]
        if from_city is not current:
            continue
        to_city = connectionL[1]
        cost = connectionL[2]
        print("Processing: ", from_city, " -> ", to_city, "with cost: ", cost)
        if to_city not in visited and cost < selected_cost:
            selected_cost = cost
            selected_node = to_city
    # As we found the next node add it to visited and add the cost to the total_cost
    if selected_node == "":
        print("No node selected")
        return
    visited.append(selected_node)
    print("Selected ", current, " -> ", selected_node,
          "COST: ", total_cost+selected_cost)
    print(visited)
    TSP(connection_list, selected_node, start,
        visited, total_cost+selected_cost, nodes_count)


visited = [start]
TOTAL_COST = 0
TSP(connection_list, start, start, visited, TOTAL_COST, nodes_count)