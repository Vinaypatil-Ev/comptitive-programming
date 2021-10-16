# recurive solution
def has_path_recur(graph, src, dst):
    if src == dst:
        return True
    for i in graph[src]:
        if has_path_recur(graph, i, dst):
            return True
    return False

# iterative solution
def has_path(graph, src, dst):
    q = [src]
    while q:
        curr = q.pop(0)
        if curr == dst:
            return True
        for i in graph[curr]:
            q.append(i)
    return False
        


if __name__ == "__main__":
    graph = {
        "a": ["b", "h"],
        "b": ["e"],
        "c": ["d", "f"],
        "d": ["g"],
        "g": ["f"],
        "f": [],
        "e": ["f", "h"],
        "h": [],
    }
    src = "a"
    dst = "f"
    # x = has_path_recur(graph, src, dst)
    x = has_path(graph, src, dst)
    if x:
        print(f"It has path between {src}, {dst}")
    else:
        print("no path")