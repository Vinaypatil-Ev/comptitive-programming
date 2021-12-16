from Graph import Graph
def dfs(graph, node, color):
    color[node] = 1

    for adjnode in graph[node]:
        if color[adjnode] == 0:
            if dfs(graph, node, color):
                return True
        if color[adjnode] == 1:
            return True
    color[node] = 2
    return False


def is_cycle(graph, v):
    color = [0] * v

    for i in range(v):
        if color[i] == 0:
            if dfs(graph, node, color):
                return True
    return False


if __name__ == "__main__":
    g = Graph(4)