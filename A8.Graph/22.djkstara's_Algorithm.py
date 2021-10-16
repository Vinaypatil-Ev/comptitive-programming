class Graph:
    def __init__(self, V, E):
        self.V = V
        self.E = E
        self.graph = [[0] * V for _ in range(V)]
        self.parent = [-1] * V
        self.visited = set()
        self.dist = [float("inf")] * V
        

    def add_edge(self, a, b, w):
        self.graph[a][b] = w
        self.graph[b][a] = w

    def find_min_vertex(self):
        minimum = float("inf")
        vetex = None
        for i in range(self.V):
            if i not in self.visited and self.dist[i] < minimum:
                vetex = i
                minimum = self.dist[i]
        return vetex
    
    def dj(self, start):
        self.dist[start] = 0
        for _ in range(self.V - 1):
            u = self.find_min_vertex()
            self.visited.add(u)
            for v in range(self.V):
                if v not in self.visited and self.dist[u] + self.graph[u][v] < self.dist[v] and self.graph[u][v] != 0:
                    self.dist[v] = self.dist[u] + self.graph[u][v]
                    self.parent[v] = u
        return self.dist
    
if __name__ == "__main__":
    v, e = list(map(int, input().strip().split()))
    start = int(input())
    g = Graph(v, e)
    for i in range(e):
        a, b, w = list(map(int, input().strip().split()))
        g.add_edge(a, b, w)
    x = g.dj(start)
    for i in x:
        print(i, end=" ")
        
        