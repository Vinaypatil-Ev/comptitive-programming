inputLine = lambda: list(map(int, input().split()))
class Graph:
    def __init__(self, V, E):
        self.V = V
        self.E = E
        self.graph = [[] for _ in range(V)]
        self.disc = [-1] * V
        self.lows = [-1] * V
        self.instack = [False] * V
        self.st = []
        self.scc = 0
        self.compo = []
        self.time = 0
    def add_edge_d(self, a, b):
        self.graph[a].append(b)
    def dfs(self, node):
        self.lows[node] = self.disc[node] = self.time
        self.time += 1
        self.st.append(node)
        self.instack[node] = True
        for adjnode in self.graph[node]:
            if self.disc[adjnode] == -1:
                self.dfs(adjnode)
                self.lows[node] = min(self.lows[node], self.lows[adjnode])
            else:
                if self.instack[adjnode]:
                    self.lows[node] = min(self.lows[node], self.disc[adjnode]) 
        if self.lows[node] == self.disc[node]:
            compo = []
            while len(self.st) - 1 != node:
                self.instack[len(self.st) - 1] = False
                x = self.st.pop()
                compo.append(x)
            self.instack[len(self.st) - 1] = False
            x = self.st.pop()
            compo.append(x)
            self.compo.append(compo)
            self.scc += 1
            
    def tarjan(self):
        for node in range(self.V):
            if self.disc[node] == -1:
                self.dfs(node)
                
    
    
if __name__ == "__main__":
    v, e = inputLine()
    g = Graph(v, e)
    for _ in range(e):
        a, b = inputLine()
        g.add_edge_d(a, b)
    g.tarjan()
    print(g.scc)
    # print(g.compo)