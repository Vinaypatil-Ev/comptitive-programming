from collections import defaultdict as ddict
import heapq as h
class Graph:
    def __init__(self, V, E):
        self.V = V
        self.E = E
        self.graph = ddict(lambda: [])
        self.pq = []
        self.visited = set()
    def add_edge_d(self, a, b, w):
        if a not in self.graph:
            self.graph[a] = []
        if b not in self.graph:
            self.graph[b] = []
        self.graph[a].append((a, b, w))
        self.graph[b].append((b, a, w))
    def add_edge_pq(self, node):
        self.visited.add(node)
        for edge in self.graph[node]:
            a, b, wt = edge
            if b not in self.visited:
                self.pq.append((wt, a, b))
    def prim(self):
        j = 0
        mstcost = 0
        self.add_edge_pq(0)
        while self.pq and j < self.V - 1:
            wt, fr, to = h.heappop(self.pq)
            if to in self.visited:
                continue
            mstcost += wt
            j += 1
            self.add_edge_pq(to)
        return mstcost
    
    
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
        g.add_edge_d(a-1, b-1, w)
    x = g.prim()
    print(x)
            