from collections import defaultdict as ddict
from typing_extensions import get_args


class Graph:
    def __init__(self, vert):
        self.vert = vert
        self.V = len(self.vert)
        self.graph = ddict(lambda: [])
    def __str__(self):
        return str(self.graph)
        
    def add_edge(self, a, b, w):
        if a not in self.graph:
           self.graph[a] = []
        self.graph[a].append((b, w)) 
    def from_arr(self, arr, simple=True):
        self.graph.clear()
        if simple:
            for i in range(2, len(arr), 3):
                a, b, w = arr[i - 2], arr[i - 1], arr[i]
                self.add_edge(a, b, w)
    def top_sort(self):
        visited = set()
        orders = [None] * self.V
        i = self.V - 1
        for node in self.vert:
            if node not in visited:
                i = self.explore_neighbour(self.graph, node, visited, orders, i)
        return orders
    
    def explore_neighbour(self, graph, node, visited, orders, i):
        visited.add(node)
        for adjnode in graph[node]:
            if adjnode[0] not in visited:
                i = self.explore_neighbour(graph, adjnode[0], visited, orders, i)
        orders[i] = node
        return i - 1
    
    def sssp(self, start):
        topsort = self.top_sort()
        dist = ddict(lambda: None)
        dist[start] = 0
        for node in topsort:
            if dist[node] is not None:
                for adjnode in self.graph[node]:
                    new_dist = dist[node] + adjnode[1]
                    if dist[adjnode[0]] is None:
                        dist[adjnode[0]] = new_dist
                    else:
                        dist[adjnode[0]] = min(dist[adjnode[0]], new_dist)
        return dist
    

            
    


if __name__ == "__main__":
    vert = ["a", "b", "c", "d", "e", "f", "g", "h"]
    arr = ["a", "b", 3, "a", "c", 6, "b", "c", 4, "b", "d", 4, "b", "e", 11, "c", "d", 8, "c", "g", 11, "d", "g", 2, "d", "e", -4, "d", "f", 5, "e", "h", 9, "f", "h", 1, "g", "h", 2]
    g = Graph(vert)
    g.from_arr(arr)
    print(g.top_sort())
    print(g.sssp("a")["h"], "shortest_path")
    for i in range(2, len(arr), 3):
        arr[i] = arr[i] * -1
    g.from_arr(arr)
    print(g.sssp("a")["h"] * -1, "longest path")