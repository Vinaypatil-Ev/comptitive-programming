class Graph:
    def __init__(self, V):
        self.V = V
        self.graph = [[] for _ in range(V)]
        self.stack = [False] * V
    def __str__(self):
        return str(self.graph)
    def add_edge(self, a, b):
        self.graph[a].append(b)
    def from_arr(self, arr):
        for i in range(1, len(arr), 2):
            a, b = arr[i - 1], arr[i]
            self.add_edge(a, b)
    def dc(self, graph, start, visited, stack):
        if start not in visited:
            visited.add(start)
            stack[start] = True
            for adjnode in graph[start]:
                if stack[adjnode]:
                    return True
                if adjnode not in visited:
                    return self.dc(graph, adjnode, visited, stack)
            stack[start] = False
            return False
    def detect_cycle(self):
        visited = set()
        for i in range(self.v):
            if i not in visited:
                if self.dc(self.graph, 0, set(), self.stack):
                    return True
        return False
        
        


if __name__ == "__main__":
    # arr = [0, 1, 0, 2, 1, 0, 2, 0, 2, 3, 3, 3]
    arr = [0, 1, 0, 2, 2, 1, 1, 3]
    g = Graph(4)
    g.from_arr(arr)
    g.detect_cycle()