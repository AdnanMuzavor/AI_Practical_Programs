
#Unsolved
#puzzle = [[2,8,3], [1,6,4], [7,0,5]]
#goal = [[1,2,3], [8,0,4], [7,6,5]]
#puzzle = [[2, 1, 3], [4, 0, 5], [8, 6, 7]] 

#Solved
# puzzle=[[1,2,3],[4,5,6],[7,0,8]]
# goal=[[1,2,3],[4,5,6],[7,8,0]]


max_count = 0


def display(puzzle):
    for row in puzzle:
        print(row)
    print("---------------------------------------")    


def compare(puzzle, goal):
    match = 0
    for i in range(3):
        for j in range(3):
            if puzzle[i][j] == goal[i][j]:
                match = match+1
    return match



def move_dash(iter, puzzle, goal, generated_states,x,y):
    if iter==10:
        return
    print(
        f"\n--------------I T E R {iter}-----------------")

    print("Dash found at: ", x, y)
    i = 0
    
    # Move dash
    d_X = [0, 1, -1, 0]
    d_y = [1, 0, 0, -1]
    
    # To have the next puzzle with maximum weight
    max_match_count = 0
    
    next_puzzle = []
    
    selected_x, selected_y = -1, -1
    
    for i in range(4):
        # get new positions for dash
        new_x = x+d_X[i]
        new_y = y+d_y[i]
        # validate positions
        if new_x < 0 or new_x >= 3 or new_y < 0 or new_y >= 3:
            continue
        
        # print position selected
        print("____Moving dash towards: ", new_x, new_y,"____")
        
        # update the puzzle
        num = puzzle[new_x][new_y]
        puzzle[new_x][new_y] = 0
        puzzle[x][y] = num
        
        #Generating puzzle string
        puzzle_str=str(puzzle)
        
   
        #If this is repeated state then dont consider it
        if puzzle_str in generated_states:
            print("--> R E P E A T E D  <--")
            
            # restore puzzle matrix
            num = puzzle[x][y]
            puzzle[new_x][new_y] = num
            puzzle[x][y] = 0
            continue;
        else:
            generated_states.append(puzzle_str)
    
        # get weight
        weight_cost = compare(puzzle, goal)

        # ckeep track of matrix with max weight
        if weight_cost > max_match_count:
            max_match_count = weight_cost
            next_puzzle = []
            for i in range(3):
                row = []
                for j in range(3):
                    row.append(puzzle[i][j])
                next_puzzle.append(row)
            selected_x = new_x
            selected_y = new_y
            
          
        print(
            f"Current matrix generated is: {puzzle}  wt(m {i} ) : ", weight_cost)

        # restore puzzle matrix
        num = puzzle[x][y]
        puzzle[new_x][new_y] = num
        puzzle[x][y] = 0

        i = i+1


    # Otherise print the matrix selected
    print("\n___________SELECTED______________")
    display(next_puzzle)
    print("cost: ",max_match_count)
    
    # Update the puzzle to undergo next iteration
    puzzle = next_puzzle
    
    # match_count is < 9 proceed next iter
    if max_match_count < 9:
        move_dash(iter+1,puzzle, goal, generated_states,selected_x,selected_y)
    elif max_match_count==9:
        print("Puzzle solved")

#Take input
puzzle=[]
goal=[]
print("Enter the puzzle")
for i in range(3):
    row=[int(item) for item in input(f"Enter row{i+1}: ").split(" ")]
    puzzle.append((row))
    
print("Enter the goal")
for i in range(3):
    row=[int(item) for item in input(f"Enter row{i+1}: ").split(" ")]
    goal.append((row))
    
#To keep all generated sattes
generated_states=[]
generated_states.append(str(puzzle))

x,y,i=0,0,0
for row in puzzle:
    x=i
    if 0 in row:
        y=row.index(0)
        break
    i=i+1 

move_dash(1, puzzle, goal, generated_states,x,y)