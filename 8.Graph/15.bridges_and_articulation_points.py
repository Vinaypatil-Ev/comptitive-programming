from collections import defaultdict as ddict
class Graph:
    def __init__(self, V):
        self.V = V
        self.graph = ddict(lambda: [])
        self.id = 0
    def add_edge(self, a, b):
        if a not in self.graph:
            self.graph[a] = []
        self.graph[a].append(b)
    def from_arr(self, arr):
        for i in range(1, len(arr), 2):
            a, b = arr[i - 1], arr[i]
            self.add_edge(a, b)
    def dfs(self, node, parent, ids, lows, visited, bridges, id):
        id += 1
        lows[node] = ids[node] = id
        visited.add(node)
        for adjnode in self.graph[node]:
            if adjnode == parent:
                continue
            if adjnode not in visited:
                self.dfs(adjnode, node, ids, lows, visited, bridges, id)
                lows[node] = min(lows[node], lows[adjnode])
                if ids[node] < lows[adjnode]:
                    bridges.append(node)
                    bridges.append(adjnode)
            else:
                ids[node] = min(lows[node], ids[adjnode])
        
    def find_brides(self):
        ids = [None] * self.V
        lows = [None] * self.V
        visited = set()
        bridges = []
        id = 0
        for i in range(self.V):
            if i not in visited:
                self.dfs(i, -1, ids, lows, visited, bridges, id)
        print(bridges)

    def dfs(self, node, parent, ids, lows, visited, bridges, id):
        id += 1
        lows[node] = ids[node] = id
        visited.add(node)
        for adjnode in self.graph[node]:
            if adjnode == parent:
                continue
            if adjnode not in visited:
                self.dfs(adjnode, node, ids, lows, visited, bridges, id)
                lows[node] = min(lows[node], lows[adjnode])
                if ids[node] < lows[adjnode]:
                    bridges.append(node)
                    bridges.append(adjnode)
            else:
                ids[node] = min(lows[node], ids[adjnode])
        
    def find_brides(self):
        ids = [None] * self.V
        lows = [None] * self.V
        visited = set()
        bridges = []
        id = 0
        for i in range(self.V):
            if i not in visited:
                self.dfs(i, -1, ids, lows, visited, bridges, id)
        print(bridges)
        
    
            


if __name__ == "__main__":
    n = 9
    arr = [0, 1, 1, 2, 2, 0, 2, 5, 5, 6, 6, 7, 7, 8, 8, 5, 2, 3, 3, 4]
    g = Graph(n)
    g.from_arr(arr)
    g.find_brides()