inputLine = lambda: list(map(int, input().split()))

class Graph:
    def __init__(self, V, E):
        self.V = V
        self.E = E
        self.graph = [[] for _ in range(V)]
        self.scc = 0
        self.visited = set()
        self.st = []
    def add_edge_d(self, a, b):
        self.graph[a].append(b)
    
    def dfs(self, node):
        self.visited.add(node)
        for adjnode in self.graph[node]:
            if adjnode not in self.visited:
                self.dfs(adjnode)
        self.st.append(node)
        
    def dfs2(self, node):
        self.visited.add(node)
        for adjnode in self.graph[node]:
            if adjnode not in self.visited:
                self.dfs(adjnode)
    
    def reverse(self):
        graph = [[] for _ in range(self.V)]
        for node in range(self.V):
            for adjnode in self.graph[node]:
                graph[adjnode].append(node)
        self.graph = graph
    def kosaraju(self):
        """
        dfs()
        reverse()
        dfs()
        """
        for node in range(self.V):
            if node not in self.visited:
                self.dfs(node)
        self.reverse()
        self.visited.clear()
        while self.st:
            node = self.st.pop()
            if node not in self.visited:
                self.dfs2(node)
                self.scc += 1        

if __name__ == "__main__":
    v, e = inputLine()
    g = Graph(v, e)
    for _ in range(e):
        a, b = inputLine()
        g.add_edge_d(a, b)
    g.kosaraju()
    print(g.scc)