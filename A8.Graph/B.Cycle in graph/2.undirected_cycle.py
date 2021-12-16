from Graph import Graph

def dfs(graph, node, vis, parent):
    vis[node] = True
    for adjnode in graph[node]:
        if not vis[adjnode]:
            if dfs(graph, adjnode, vis, node):
                return True
        if parent != adjnode:
            return True
    return False


def is_cycle(graph, v):
    vis = [False] * v

    for i in range(v):
        if not vis[i]:
            if dfs(graph, i, vis, -1):
                return True
    return False



if __name__ == "__main__":
    g = Graph(4, True)
    g.from_arr([0, 1, 0, 2, 1, 2, 2, 0, 2, 3, 3, 3])
    x = is_cycle(g.graph, g.v)
    print(x)