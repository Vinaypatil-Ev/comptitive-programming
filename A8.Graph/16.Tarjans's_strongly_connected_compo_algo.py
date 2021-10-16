from collections import defaultdict as ddict
class Graph:
    uv = -1
    ssc = 0
    def __init__(self, V):
        self.V = V
        self.graph = ddict(lambda: [])
        
        
    def __str__(self):
        return str(self.graph)
    def add_edge(self, a, b):
        if a not in self.graph:
            self.graph[a] = []
        self.graph[a].append(b)
    
    def from_arr(self, arr):
        for i in range(1, len(arr), 2):
            a, b = arr[i - 1], arr[i]
            self.add_edge(a, b)
    def ta(self, node, stack, onstack, ids, lows, id):
        stack.append(node)
        onstack[node] = True
        ids[node] = lows[node] = id
        id += 1
        # explore all adjnodes of curr node
        for adjnode in self.graph[node]:
            if ids[adjnode] == self.uv:
                self.ta(adjnode, stack, onstack, ids, lows, id)
            if onstack[adjnode]:
                lows[node] = min(lows[node], lows[adjnode])
        if ids[node] == lows[node]:
            snode = stack.pop()
            while snode != node:
                onstack[snode] = False
                lows[snode] = ids[node]
                snode = stack.pop()
                
            self.ssc += 1
        
        
    def find_ssc(self):
        id = 0
        ids = [-1] * self.V
        lows = [0] * self.V
        onstack = [False] * self.V
        stack = []
        
        for node in range(self.V):
            if ids[node] == self.uv:
                self.ta(node, stack, onstack, ids, lows, id)
        return self.ssc
            


if __name__ == "__main__":
    n = 5
    arr = [1, 0, 0, 2, 2, 1, 0, 3, 3, 4]
    g = Graph(n)
    g.from_arr(arr)
    print(g.find_ssc())
    