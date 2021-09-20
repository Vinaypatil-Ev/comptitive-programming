class Graph:
    def __init__(self, V, E):
        self.V = V
        self.E = E
        self.graph = []
        self.parent = [-1] * V
        self.dist = [0] * V
        self.rank = [0] * V
        self.mst = []
    def add_edge_d(self, a, b, w):
        self.graph.append((a, b, w))
    def find(self, v):
        if self.parent[v] == -1:
            return v
        u = self.find(self.parent[v])
        self.parent[v] = u
        return u
    def union(self, ap, bp):
        if self.rank[ap] > self.rank[bp]:
            self.parent[bp] = ap
        elif self.rank[ap] < self.rank[bp]:
            self.parent[ap] = bp
        else:
            self.parent[ap] = bp
            self.rank[bp] += 1
    def kruskal(self):
        self.graph = sorted(self.graph, key=lambda x: x[2])
        i = j = 0
        while i < self.V and j < self.E:
            ap = self.find(self.graph[i][0])
            bp = self.find(self.graph[i][1])
            if ap == bp:
                j += 1
                continue
            self.union(ap, bp)
            self.dist[i] = self.graph[i][2]
            self.mst.append(self.graph[i][2])
        return self.mst
            
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
    x = g.kruskal()
    print(sum(x))
    
       
# class Graph:
#     def __init__(self, V, E):
#         self.V = V
#         self.E = E
#         self.edge_list = []
#         self.parent = [-1] * V
#         self.rank = [0] * V
#         self.mst = []
#     def add_edge_d(self, edge):
#         self.edge_list.append(edge)
    
#     def find(self, v):
#         if self.parent[v] == -1:
#             return v 
#         self.parent[v] = self.find(self.parent[v])
#         return v
    
#     def union(self, fromp, top):
#         if self.rank[fromp] > self.rank[top]:
#             self.parent[top] = fromp
#         elif self.rank[fromp] < self.rank[top]:
#             self.parent[fromp] = top
#         else:
#             self.parent[fromp] = top
#             self.rank[top] += 1
#     def kruskal(self):
#         self.edge_list = sorted(self.edge_list, key=lambda a: a[2])
#         i = j = 0
#         while i < self.V - 1 and j < self.E:
#             fromp = self.find(self.edge_list[j][0])
#             top = self.find(self.edge_list[j][1])
#             if fromp == top:
#                 j += 1
#                 continue
#             self.union(fromp, top)
#             self.mst.append(self.edge_list[i][2])
#             i += 1
    

# print()