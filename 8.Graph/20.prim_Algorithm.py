class Graph:
    def __init__(self, V, E):
        self.V = V
        self.E = E
        self.edge_list = []
        self.parent = [-1] * V
        self.rank = [0] * V
        self.mst = []
    def add_edge_d(self, edge):
        self.edge_list.append(edge)
    
    def find(self, v):
        if self.parent[v] == -1:
            return v 
        self.parent[v] = self.find(self.parent[v])
        return v
    
    def union(self, fromp, top):
        if self.rank[fromp] > self.rank[top]:
            self.parent[top] = fromp
        elif self.rank[fromp] < self.rank[top]:
            self.parent[fromp] = top
        else:
            self.parent[fromp] = top
            self.rank[top] += 1
    def kruskal(self):
        self.edge_list = sorted(self.edge_list, key=lambda a: a[2])
        i = j = 0
        while i < self.V - 1 and j < self.E:
            fromp = self.find(self.edge_list[j][0])
            top = self.find(self.edge_list[j][1])
            if fromp == top:
                j += 1
                continue
            self.union(fromp, top)
            self.mst.append(self.edge_list[i][2])
            i += 1
    


if __name__ == "__main__":
    v, e = list(map(int, input().split()))
    g = Graph(v, e)
    for i in range(e):
        a, b, w = list(map(int, input().split()))
        g.add_edge_d((a, b, w))
    g.kruskal()
    print(sum(g.mst))
    # print(g.edge_list)
# arr = [1, 2, 1, 1, 3, 9, 5, 6, 12, 2, 3, 6, 1, 3, 4, 1, 9, 7, 7, 1, 13, 3, 4, 8]
# edge = []
# for i in range(2, len(arr), 3):
#     edge.append((arr[i - 2], arr[i - 1], arr[i]))
    

# print()