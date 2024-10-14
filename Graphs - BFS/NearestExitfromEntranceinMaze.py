from collections import deque

def nearestExit(maze, entrance):
    rows, cols = len(maze), len(maze[0])
    start_row, start_col = entrance
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up, down, left, right
    
    # Initialize queue for BFS with the starting point (entrance)
    queue = deque([(start_row, start_col, 0)])  # (row, col, steps)
    visited = set([(start_row, start_col)])  # to avoid revisiting
    
    # BFS loop
    while queue:
        row, col, steps = queue.popleft()
        
        # Check all 4 directions
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            
            # Check if new position is within the bounds of the maze and is an empty cell
            if 0 <= new_row < rows and 0 <= new_col < cols and maze[new_row][new_col] == '.':
                # If this is an exit (on the boundary and not the entrance), return the steps
                if (new_row in [0, rows - 1] or new_col in [0, cols - 1]) and (new_row, new_col) != (start_row, start_col):
                    return steps + 1
                
                # If this is not visited, add it to the queue and mark it as visited
                if (new_row, new_col) not in visited:
                    visited.add((new_row, new_col))
                    queue.append((new_row, new_col, steps + 1))
    
    # If no exit is found
    return -1

maze = [["+", "+", ".", "+"],
        [".", ".", ".", "+"],
        ["+", "+", "+", "."]]
entrance = [1, 2]
result = nearestExit(maze, entrance)
print(result)
