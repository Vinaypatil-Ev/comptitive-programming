class Graph:
    def __init__(self, V, E):
        self.V = V
        self.E = E
        self.graph = [[0] * V for _ in range(V)]
        self.parent = [-1] * V
        self.dist = [float("inf")] * V
        self.visited = set()
    def add_edge_d(self, a, b, w):
        try:
            self.graph[a][b] = w
            self.graph[b][a] = w
        except:
            print(a, b, self.V)
            exit()
    def find_min_node(self):
        minimum = float("inf")
        vertex = None
        for i in range(self.V):
            if i not in self.visited and self.dist[i] < minimum:
                vertex = i
                minimum = self.dist[i]
        return vertex
    def prim(self):
        self.dist[0] = 0
        for _ in range(self.V - 1):
            u = self.find_min_node()
            self.visited.add(u)                
            for v in range(self.V):
                try:
                    if self.graph[u][v] != 0 and v not in self.visited and self.graph[u][v] < self.dist[v]:
                        self.dist[v] = self.graph[u][v]
                        self.parent[v] = u
                except Exception as p:
                    pass
        return self.dist    


if __name__ == "__main__":
    flag = False
    size = list(map(int, input().split()))
    if len(size) == 3:
        flag = True
        v, e, i = size
    else:
        v, e = size
    
    g = Graph(v, e)
    
    for i in range(e):
        a, b, w = list(map(int, input().split()))
        if flag:
            a -= 1
            b -= 1
        g.add_edge_d(a, b, w)
    x = g.prim()
    print(sum(x))