from Graph import Graph
def dfs(graph, node):
    vis[node] = True
    for adjnode in graph[node]:
        if not vis[adjnode]:
            dfs(graph, adjnode)
    order.append(node)
        

def toposort(n, graph):
    global vis, order
    vis = [False] * n
    order = []
    for i in range(n):
        if not vis[i]:
            dfs(graph, i)
    return order[::-1]
        

def init():
    n = 6
    g = Graph(n, True)
    g.from_arr([5, 2, 5, 0, 4, 0, 4, 1, 2, 3, 3, 1])
    return g

if __name__ == "__main__":
    ans = [5, 4, 2, 3, 1, 0]
    g = init()
    print(g.graph)
    print(ans, toposort(g.v, g.graph))