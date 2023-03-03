# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 09:10:09 2023

@author: Student
"""


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


"""tree={
      'A':['B','C'],
      'B':['D','E','A'],
      'C':['F','G','A','E'],
      'D':['B'],
      'E':['B','C'],
      'F':['C'],
      'G':['C']
      }"""
tree={}
#bfs(start,tree)

#bfs_search(start, goal, tree)

while True:
    choice=input("Menu: \n 1) Create Graph 2) Display BFS 3) Search Goal node  4) Exit")
    choice=int(choice)

    if choice == 1:
            nodes=int(input("Enter number of edges: "))
            while nodes:
                n,m=input("Enter the adjacent nodes: ").split(" ")
                if n in tree:
                  tree[n].append(m)
                else:
                  tree[n]=[m]
                if m in tree:
                  tree[m].append(n)
                else:
                  tree[m]=[n]
                nodes=nodes-1      
           
    elif choice == 2:
            start=input("Enter the start node : ") 
            bfs(start, tree)
    elif choice == 3:
            start,goal=input("Enter the start node and goal node: ").split(" ") 
            bfs_search(start, goal, tree)
    elif choice == 4:
            break
    else:
            print("Invalid input")