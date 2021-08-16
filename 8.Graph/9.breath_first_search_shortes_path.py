# def explore(grid, R, C, visited, rr, cc, dist, q):
#     dr = [-1, 1, 0,  0]
#     dc = [0, 0, -1, 1]
#     for i in range(4):
#         r = rr + dr[i]
#         c = cc + dc[i]
#         if r < 0 or c < 0 or r >= R or c >= C or grid[r][c] == "#" or (r, c) in visited:
#             continue
#         q.append((r, c, dist + 1))
#         visited.add((r, c))
        
                      
# def grid_shortest_path(grid, start, end):
#     R = len(grid)
#     C = len(grid[0])
#     q = [(0, 0, 0)]
#     visited = set()
#     while q:
#         block = q.pop(0)
#         rr, cc, dist = block
#         if grid[rr][cc] == end:
#             return dist
#         explore(grid, R, C, visited, rr, cc, dist, q)
#     return 0


        
                      
def grid_shortest_path2(grid, start, end):
    R = len(grid)
    C = len(grid[0])
    q = [(0, 0, 0)]
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    visited = {(0, 0)}
    path = {(0, 0): -1}
    while q:
        curr = q.pop(0)
        cr, cc, dist = curr
        if grid[cr][cc] == end:
            reached_end = True
            break
        for i in range(4):
            r = cr + dr[i]
            c = cc + dc[i]
            if r < 0 or c < 0 or r >= R or c >= C or grid[r][c] == "#" or (r, c) in visited:
                continue
            q.append((r, c, dist + 1))
            visited.add((r, c))
            path[(r, c)] = (cr, cc)

    if reached_end:
        p = []
        v = (4, 3)
        while v != -1:
            p.append(v)
            v = path[v]
        p.reverse()
        return dist, p
    return 0
        
        
        
        



if __name__ == "__main__":
    grid = [
        ["S", ".", ".", "#", ".", ".", ".",],
        [".", "#", ".", ".", "#", ".", ".",],
        [".", "#", ".", ".", ".", ".", ".",],
        [".", ".", "#", "#", ".", ".", ".",],
        ["#", ".", "#", "E", ".", ".", "#",]
    ]
    start = "S"
    end = "E"
    # x = grid_shortest_path(grid, start, end)
    # if x:
    #     print(f"shortes distance between {start}, {end}: {x}")
    # else:
    #     print("No shortest path")
    x, path = grid_shortest_path2(grid, start, end)
    if x:
        print(f"shortes distance between {start}, {end}: {x}")
        print(path)
    else:
        print("No shortest path")