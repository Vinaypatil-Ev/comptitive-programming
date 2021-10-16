from collections import defaultdict as ddict
class Graph:
    def __init__(self, V, E):
        self.V = V
        self.E = E
        self.graph = ddict(lambda: [])
    def __str__(self):
        return str(self.graph)
    def from_arr(self, arr):
        for i in range(2, len(arr), 3):
            a, b, w = arr[i - 2], arr[i - 1], arr[i]
            if a not in self.graph:
                self.graph[a] = []
            self.graph[a].append((b, w))
        
    def sssp_bell(self, start):
        dist = [float("inf")] * self.V
        dist[start] = 0
        # update shortest distance
        for node in range(0, self.V):
            for adjnode in self.graph[node]:
                if dist[node] + adjnode[1] < dist[adjnode[0]]:
                    dist[adjnode[0]] = dist[node] + adjnode[1]
        # reapeat to find node cought in a negative cycle
        for node in range(0, self.V):
            for adjnode in self.graph[node]:
                if dist[node] + adjnode[1] < dist[adjnode[0]]:
                    dist[adjnode[0]] = float("-inf")
        print(dist)
    


if __name__ == "__main__":
    arr = [0, 1, 5, 1, 2, 20, 1, 6, 60, 2, 3, 10, 3, 2, -15, 2, 4, 75, 1, 5, 30, 5, 6, 5, 5, 4, 25, 4, 9, 100, 5, 8, 50, 6, 7, -50, 7, 8, -10]
    g = Graph(10, 13)
    g.from_arr(arr)
    g.sssp_bell(0)