def count_conn_compo(graph):
    visited = set()
    count = 0
    for node in graph.keys():
        if explore(graph, node, visited):
            count += 1
    return count

def explore(graph, node, visited):
    if node in visited:
        return False
    visited.add(node)
    for adjnode in graph[node]:
        explore(graph, adjnode, visited)
    return True

if __name__ == "__main__":
    graph = {
        "a": ["b", "b", "c", "d"],
        "b": ["a"],
        "c": ["a"],
        "d": ["a"],
        "g": ["f"],
        "f": ["g", "h"],
        "e": [],
        "h": ["f"],
    }
    x = count_conn_compo(graph)
    print(f"There are {x} components")