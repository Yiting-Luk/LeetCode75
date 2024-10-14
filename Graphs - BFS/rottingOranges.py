from collections import deque

def orangesRotting(grid):
    rows = len(grid)
    cols = len(grid[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up, down, left, right
    queue = deque()
    fresh_oranges = 0 # number of fresh oranges
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                queue.append((r, c, 0)) # 0 = time
            elif grid[r][c] == 1:
                fresh_oranges += 1

    if fresh_oranges == 0:
        return 0

    while queue:
        r, c, time = queue.popleft()
        for dr, dc in directions:
            nr = r + dr
            nc = c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                grid[nr][nc] = 2
                fresh_oranges -= 1
                queue.append((nr, nc, time + 1)) # time is not updated, so all the neighbours record the same minutes_passed
    
    if fresh_oranges > 0:
        return -1
    
    return time

grid = [[2,1,1],[1,1,0],[0,1,1]]
result = orangesRotting(grid)
print(result)
