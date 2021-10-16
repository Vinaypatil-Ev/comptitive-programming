def explore(grid, R, C, visited, rr, cc, dist, q):
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
#     reached_end = False
#     left_nodes = 1
#     next_nodes = 0
#     while q:
#         block = q.pop(0)
#         rr, cc, dist = block
#         if grid[rr][cc] == end:
#             # return dist
#             reached_end = True
#             break
#         explore(grid, R, C, visited, rr, cc, dist, q)
#     return 0