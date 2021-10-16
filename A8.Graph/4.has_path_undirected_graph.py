def convert_adj_list(edge_list):
    graph = {}
    for i in edge_list:
        a, b = i
        if a not in graph:
            graph[a] = []
        if b not in graph:
            graph[b] = []
        graph[a].append(b)
        graph[b].append(a)
    return graph

def has_path(graph, src, dst, visited: set):
    if src == dst:
        return True
    if src in visited:
        return False
    visited.add(src)
    for i in graph[src]:
        if has_path(graph, i, dst, visited):
            return True
    return False
        

if __name__ == "__main__":
    edge_list = [
        ["a", "b"],
        ["b", "c"],
        ["a", "h"],
        ["b", "e"],
        ["c", "d"],
        ["c", "f"],
        
    ]
    graph = convert_adj_list(edge_list)
    print(graph)
    src = "a"
    dst = "f"
    x = has_path(graph, src, dst, set())
    if x:
        print(f"has path betn {src}, {dst}")
    else:
        print("no path")