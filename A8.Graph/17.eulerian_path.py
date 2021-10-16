from collections import defaultdict as ddict
class Graph:
    def __init__(self, V, E):
        self.V = V
        self.E = E
        self.graph = ddict(lambda: [])
        self._out = None
        self._in = None
        self._edge_count = 0
        self._path = []
        self._is_set = False
    def add_directed_edge(self, a, b):
        if a not in self.graph:
            self.graph[a] = []
        self.graph[a].append(b)
    def from_arr(self, arr):
        for i in range(1, self.V):
            a, b = arr[i - 1], arr[i]
            self.add_directed_edge(a, b)
    def setup(self):
        self.is_set = True
        # count In and Out degree
        self._out = [0] * self.V
        self._in = [0] * self.V
        for node in range(self.V):
            for adjnode in self.graph[node]:
                self._out[node] += 1
                self._in[adjnode] += 1
                self._edge_count += 1
    def has_graph_eulerian_path(self):
        if self._edge_count == 0:
            return False
        start_node = end_node = 0
        for i in range(self.V):
            if self._in[i] - self._out[i] > 1 or self._out[i] - self._in[i] > 1:
                return False
            elif self._out[i] - self._in[i] == 1:
                start_node += 1
            elif self._in[i] - self._out[i] == 1:
                end_node += 1
            return (start_node == 0 and end_node == 0) or (start_node == 1 and end_node == 1)
    def find_start_node(self):
        start = 0
        for i in range(self.V):
            if self._out[i] - self._in[i] == 1:
                return i
            if self._out[i] > 0:
                start = i
        return start
    
    def dfs(self, node):
        while self._out[node] != 0:
            self._out[node] -= 1
            adjnode = self.graph[node][self._out[node]]
            self.dfs(adjnode)
            self._path.insert(0, node)
    def get_eulerian_path(self):
        if not self._is_set:
            self.setup()
        
        if not self.has_graph_eulerian_path():
            return False
        
        self.dfs(self.find_start_node())
        
        if len(self._path) == self._edge_count + 1:
            return None
        
        return self._path
        
if __name__ == "__main__":
    v = 7
    node_edge_list = [1, 2, 1, 3, 2, 2, 2, 4, 3, 1, 3, 2, 3, 5, 4, 3, 4, 6, 5, 6, 6, 3]
    E = len(node_edge_list) // 2
    print(E)
    g = Graph(v, E)
    g.from_arr(node_edge_list)
    x = g.get_eulerian_path()
    print(x)
        
    