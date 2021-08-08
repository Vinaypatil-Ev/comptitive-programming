def bfs_graph(graph, source):
    queue = [source]
    while queue:
        curr = queue.pop(0)
        print(curr, " -> ", end="")
        for i in graph[curr]:
            queue.append(i)

if __name__ == "__main__":
    graph = {
        "a": ["b", "c"],
        "b": ["d"],
        "c": ["e"],
        "d": ["f"],
        "e": [],
        "f": [],
    }
    bfs_graph(graph, "a")