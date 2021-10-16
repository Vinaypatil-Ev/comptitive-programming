def create_graph(edge_list):
    graph = {}
    for edges in edge_list:
        a, b = edges
        if a not in graph:
            graph[a] = []
        if b not in graph:
            graph[b] = []
        graph[a].append(b)
        graph[b].append(a)
    return graph
            

def shortest_path(graph, src, dst):
    visited = set()
    q = [(src, 0)]
    while q:
        curr = q.pop(0)
        node, distance = curr
        if node == dst:
            return distance
        for adjnode in graph[node]:
            if adjnode not in visited:
                visited.add(adjnode)
                q.append((adjnode, distance + 1))
    return -1
    
        






if __name__ == "__main__":
    edges = [
                ['w', 'x'],
                ['x', 'y'],
                ['z', 'y'],
                ['z', 'v'],
                ['w', 'v']
            ]
    
    edges = [
  ['a', 'c'],
  ['a', 'b'],
  ['c', 'b'],
  ['c', 'd'],
  ['b', 'd'],
  ['e', 'd'],
  ['g', 'f']
]
    graph = create_graph(edges)
    src = "a"
    dst = "e"
    x = shortest_path(graph, src, dst)
    if x != -1:
        print(f"shortest distance between {src} {dst} is {x}")
    else:
        print("no shortest path")