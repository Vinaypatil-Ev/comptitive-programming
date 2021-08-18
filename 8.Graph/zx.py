# floyd warshwall algo
class Graph:
    def __init__(self, V):
        self.V = V
        self.graph = [[0] * self.V for _ in range(self.V)]
        self.dist = [[float("inf")] * self.V for _ in range(self.V)]
        self.next = [[0] * self.V for _ in range(self.V)]
        self.set = False
        self.solve = False
        
    def add_edge(self, a, b, w):
        self.graph[a][b] = w
    
    def create_path(self, arr):
        for i in range(2, len(arr), 3):
            a, b, w = arr[i - 2], arr[i - 1], arr[i]
            self.add_edge(a, b, w)
            
    def setup(self):
        for i in range(self.V):
            for j in range(self.V):
                if self.graph[i][j] != 0:
                    self.dist[i][j] = self.graph[i][j]
                    self.next[i][j] = j
    
    def floyd_warshall(self):
        for k in range(self.V):
            for i in range(self.V):
                for j in range(self.V):
                    if self.dist[i][k] + self.dist[k][j] < self.dist[i][j]:
                        self.dist[i][j] = self.dist[i][k] + self.dist[k][j]
                        self.next[i][j] = self.next[i][k]
        # negative cycles
        
        for k in range(self.V):
            for i in range(self.V):
                for j in range(self.V):
                    if self.dist[i][k] + self.dist[k][j] < self.dist[i][j]:
                        self.dist[i][j] = float("-inf")
                        self.next[i][j] = -1
        
    def apsp_fw(self):
        if not self.set:
            self.setup()
        if not self.solve:
            self.floyd_warshall()
            return self.dist, self.next
    
    def reconstruct_path(self, start, end):
        if not self.solve:
            self.apsp_fw()
        path = []
        if self.dist[start][end] == float("inf"):
            return path
        
        i = start
        while i != end:
            if i == -1:
                return None
            path.append(i)
            i = self.next[i][end]
        if self.dist[start][end] == -1:
            return None
        path.append(end)
        return path
    
    def find_all_pair_shortest_path(self):
        for i in range(self.V):
            for j in range(self.V):
                path = self.reconstruct_path(i, j)
                s = ""
                if path is None:
                    s = "Not exist (negative cycle case)"
                elif len(path) == 0:
                    s = "exist INFINITE(oo) no of path"
                else:
                    s = "->".join(list(map(str, path)))
                print(f"Shortest path form {i} to {j}: {s}")
                
                
if __name__ == "__main__":
    n = 7
    arr = [0, 1, 2, 0, 2, 5, 0, 6, 10, 1, 2, 2, 1, 4, 11, 2, 6, 2, 6, 5, 11, 4, 5, 1, 5, 4, -2]
    g = Graph(n)
    g.create_path(arr)
    g.find_all_pair_shortest_path()
                
                
        
        
            
            
        