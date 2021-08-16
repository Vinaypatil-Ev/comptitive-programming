from collections import defaultdict as ddict
import heapq as h

class Graph:
    def __init__(self, V):
        self.graph = ddict(lambda: [])
    def __str__(self):
        return str(self.graph)
    def from_arr(self, arr):
        for i in range(2, len(arr), 3):
            a, b, w = arr[i - 2], arr[i - 1], arr[i]
            if a not in self.graph:
                self.graph[a] = []
            self.graph[a].append((b, w))
    def sssp_dj(self, start):
        dist = ddict(lambda: None)
        path = ddict(lambda: None)
        dist[start] = 0
        visited = set()
        pq = [(0, start)]
        while pq:
            d, node = h.heappop(pq)
            visited.add(node)
            if dist[node] < d:
                continue
            for adjnode in self.graph[node]:
                if adjnode[0] not in visited:
                    new_dist = d + adjnode[1]
                    if dist[adjnode[0]] is None:
                        dist[adjnode[0]] = new_dist
                    elif new_dist < dist[adjnode[0]]:
                        dist[adjnode[0]] = new_dist
                    path[adjnode[0]] = node
                    h.heappush(pq, (new_dist, adjnode[0]))
        return dist, path
    def shortes_path(self, start, end):
        dist, path = self.sssp_dj(start)
        p = []
        i = end
        while i is not None:
            p.append(i)
            i = path[i]
        p.reverse()
        return dist, p


if __name__ == "__main__":
    arr = [0, 1, 4, 0, 2, 1, 1, 3, 1, 2, 3, 5, 3, 4, 3, 2, 1, 2]
    g = Graph(5)
    g.from_arr(arr)
    print(g.shortes_path(0, 4))
    
            
            
            
            