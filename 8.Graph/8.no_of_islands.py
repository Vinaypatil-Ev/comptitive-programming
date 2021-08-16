def count_islands(grid):
    visited = set()
    count = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if explore(grid, r, c, visited):
                count += 1
    return count
def explore(grid, r, c, visited):
    if r < 0 or r >= len(grid):
        return False
    if c < 0 or c >= len(grid[0]):
        return False
    if grid[r][c] == "W":
        return False
    if (r, c) in visited:
        return False
    visited.add((r, c))
    explore(grid, r - 1, c, visited)
    explore(grid, r, c + 1, visited)
    explore(grid, r + 1, c, visited)
    explore(grid, r, c - 1, visited)
    return True



if __name__ == "__main__":
    grid = [
            ['W', 'L', 'W', 'W', 'W'],
            ['W', 'L', 'W', 'W', 'W'],
            ['W', 'W', 'W', 'L', 'W'],
            ['W', 'W', 'L', 'L', 'W'],
            ['L', 'W', 'W', 'L', 'L'],
            ['L', 'L', 'W', 'W', 'W'],
        ]
    x = count_islands(grid)
    if x != -1:
        print(f"There are {x} islands")
    else:
        print("No island")