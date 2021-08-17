class Graph:
    def __init__(self, V):
        self.V = V
        self.graph = [[float("inf")] * V  for j in range(V)]
        # self.graph[0][0] = 0
        
        self.dist = [[0] * self.V  for _ in range(self.V)]
        self.next = [[0] * self.V  for _ in range(self.V)]
    
    def __str__(self):
        return str(self.graph)

    def add_edge(self, a, b, w):
        self.graph[a][b] = w

    def from_arr(self, arr):
        for i in range(2, len(arr), 3):
            a, b, w = arr[i - 2], arr[i - 1], arr[i]
            self.add_edge(a, b, w)

    def setup(self):
        for i in range(self.V):
            for j in range(self.V):
                if self.graph[i][j] != float("inf"):
                    self.next[i][j] = j
                self.dist[i][j] = self.graph[i][j]
                
    def apsp_fwar(self):
        self.setup()
        # execution fw for all pair short path
        for k in range(self.V):
            for i in range(self.V):
                for j in range(self.V):
                    if self.dist[i][k] + self.dist[k][j] < self.dist[i][j]:
                        self.dist[i][j] = self.dist[i][k] + self.dist[k][j]
                        self.next[i][j] = self.next[i][k]
                        
        # propogartion of negative cycles
        for k in range(self.V):
            for i in range(self.V):
                for j in range(self.V):
                    if self.dist[i][k] + self.dist[k][j] < self.dist[i][j]:
                        self.dist[i][j] = float("-inf")
                        self.next[i][j] = -1
        print(self.next)

    def shrtest_path(self, start, end):
        path = []
        if self.dist[start][end] == float("inf"):
            return path
        i = start
        while i != end:
            if i == -1:
                return None
            path.append(i)
            i = self.next[i][end]
        if self.next[i][end] == -1:
            return None
        path.append(end)
        return path
    
    def find_all_shortest_path(self):
        self.apsp_fwar()
        for i in range(self.V):
            for j in range(self.V):
                path = self.shrtest_path(i, j)
                s = ""
                if path is None:
                    s = "Has An OO Numbers of Solution! (negative cycle case)"
                elif len(path) == 0:
                    s = "not exist"
                else:
                    s = "->".join(list(map(str, path)))
                print(f"Path from {i}, {j} is {s}")
            

if __name__ == "__main__":
    n = 7
    arr = [0, 1, 2, 0, 2, 5, 0, 6, 10, 1, 2, 2, 1, 4, 11, 2, 6, 2, 6, 5, 11, 4, 5, 1, 5, 4, -2]
    g = Graph(n)
    g.from_arr(arr)
    # g.apsp_fwar()
    # g.shrtest_path(0, 4)
    # print(g.graph)
    # print()
    # print(g.next)
    # print()
    # print(g.dist)
    g.find_all_shortest_path()