def largest_component(graph, visited: set()):
    m = 0
    for node in graph:
        if node not in visited:
            x = explore(graph, node, visited)
        m = max(m, x)
    return m

def explore(graph, node, visited):
    count = 0
    if node in visited:
        return 0
    visited.add(node)
    count += 1
    for adjnode in graph[node]:
        count += explore(graph, adjnode, visited)
    return count 


if __name__ == "__main__":
    graph = {
        "0": ["1", "5", "8", "9"],
        "1": ["0", "9"],
        "5": ["0"],
        "8": ["0"],
        "9": ["1"],
        "4": ["2", "3"],
        "2": ["4", "3"],
        "3": ["2", "4"],
    }
    visited = set()
    x = largest_component(graph, visited)
    print(f"largest component is of length {x}")