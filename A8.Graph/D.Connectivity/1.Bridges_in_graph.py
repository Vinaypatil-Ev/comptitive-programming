def dfs(graph, parent, node, vis, tin, low, timer):
    vis[node] = True
    tin[node] = low[node] = timer
    timer += 1
    
    for adjnode in graph[node]:
        if parent == adjnode:
            continue
        if not vis[adjnode]:
            # parent[adjnode] = node
            dfs(graph, node, adjnode, vis, tin, low, timer)
            low[node] = min(low[node], low[adjnode])
            if low[adjnode] > tin[node]:
                print(f"Bridge {node} to {adjnode}")
        else:
            low[node] = min(low[node], tin[adjnode])
        # elif adjnode != parent:
        #     low[node] = min(low[node], tin[adjnode])


if __name__ == "__main__":
    # n = 5
    # graph = [[1, 2, 3], [0, 2], [0, 1], [0, 4], [3]]
    # graph = [[1], [0, 2], [1, 3], [2]]
    # n = 4
    n = 11
    graph = [[] for _ in range(n)]
    edge = [0, 1, 1, 2, 2, 3, 0, 3, 3, 4, 4, 5, 5, 6, 6, 7, 5, 7, 7, 8, 8, 9, 9, 10, 8, 10]
    for i in range(1, len(edge), 2):
        graph[edge[i - 1]].append(edge[i])
        graph[edge[i]].append(edge[i - 1])
    print(graph)
    vis = [False] * n
    tin = [-1] * n
    low = [-1] * n
    # parent = [-1] * n
    for i in range(n):
        if not vis[i]:
            dfs(graph, -1, i, vis, tin, low, 0)