from Graph import Graph

def dfs(graph, node, vis, todo):
    vis[node] = todo[node] = True

    for adjnode in graph[node]:
        if not vis[adjnode]:
            if dfs(graph, adjnode, adjnode, todo):
                return True
        if todo[adjnode]:
            return True
    todo[node] = False
    return False

def is_cycle(graph, v):
    vis = [False] * v
    todo = [False] * v
    for i in range(v):
        if not vis[i]:
            if dfs(graph, i, vis, todo):
                return True
    return False

if __name__ == "__main__":
    g = Graph(4)
