# iterative way and using queue
def dfs_graph(graph, source):
    stack = [source]
    while stack:
        curr = stack.pop()
        print(curr, " -> ", end="")
        for i in graph[curr]:
            stack.append(i)
def dfs_graph_recur(graph, source):
    if source:
        print(source, " -> ", end="")
        for i in graph[source]:
            dfs_graph_recur(graph, i)

if __name__ == "__main__":
    graph = {
        "a": ["b", "c"],
        "b": ["d"],
        "c": ["e"],
        "d": ["f"],
        "e": [],
        "f": [],
    }
    dfs_graph(graph, "a")
    print()
    dfs_graph_recur(graph, "a")