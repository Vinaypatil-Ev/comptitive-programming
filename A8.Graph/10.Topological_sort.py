from collections import defaultdict as ddict

def topological_sort(graph, vertices):
    n = len(vertices)
    visited = set()
    orders = [None] * n
    i = n - 1
    for node in vertices:
        if node not in visited:
            i = explore_neighbour(graph, node, visited, orders, i)
    return orders
            
def explore_neighbour(graph, node, visited, order, i):
    visited.add(node)
    for adjnode in graph[node]:
        if adjnode not in visited:
            i = explore_neighbour(graph, adjnode, visited, order, i)
    order[i] = node
    return i - 1

def create_graph(edge_list):
    graph = ddict(lambda: [])
    for edge in edge_list:
        a, b = edge
        if a not in graph:
            graph[a] = []
        graph[a].append(b)
    return graph

def create_graph2(arr):
    graph = ddict(lambda: [])
    for i in range(1, len(arr), 2):
        a, b = arr[i - 1], arr[i]
        if a not in graph:
            graph[a] = []
        graph[a].append(b)
        
    return graph
    
    

if __name__ == "__main__":
    edge_list = [
        ["c", "a"],
        ["c", "b"],
        ["a", "d"],
        ["b", "d"],
        ["e", "d"],
        ["e", "a"],
        ["e", "f"],
        ["f", "k"],
        ["f", "j"],
        ["j", "m"],
        ["d", "h"],
        ["d", "g"],
        ["g", "i"],
        ["h", "i"],
        ["h", "j"],
        ["i", "l"],
        ["j", "l"]
    ]
    # arr = ['c', 'a', 'c', 'b', 'a', 'd', 'b', 'd', 'e', 'd', 'e', 'a', 'e', 'f', 'f', 'k', 'f', 'j', 'j', 'm', 'd', 'h', 'd', 'g', 'g', 'i', 'h', 'i', 'h', 'j', 'i', 'l', 'j', 'l']
    # arr = [5, 0, 5, 2, 4, 0, 4, 1, 2, 3, 3, 1]
    v = [0, 1, 2, 3]
    edge_list = [[1,0],[2,0],[3,1],[3,2]]
    graph = create_graph(edge_list)
    # graph2 = create_graph2(arr)
    # print(graph2)
    # graph2 = create_graph2(arr, True)
    # print(graph2)
    print(topological_sort(graph, v))