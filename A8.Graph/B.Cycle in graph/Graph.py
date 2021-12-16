class Graph:
    def __init__(self, v, directed = False):
        self.directed = directed
        self.v = v
        self.graph = [[] for _ in range(v)]
    
    def form_edges(self, arr, directed = False):
        for edge in arr:
            u, v = edge
            self.graph[u].append(v)
            if not self.directed:
                self.graph[v].append(u)
    
    def from_edges(self, arr):
        for edge in arr:
            u, v = edge
            self.graph[u].append(v)
            if not self.directed:
                self.graph[v].append(u)

    def from_arr(self, arr):
        for i in range(1, len(arr)):
            u, v = arr[i - 1], arr[i] 
            self.graph[u].append(v)
            if not self.directed:
                self.graph[v].append(u)

