from Graph import Graph
import collections
def toposort(n, graph):
    topo = []
    indeg = [0] * n

    for node in range(n):
        for adjnode in graph[node]:
            indeg[adjnode] += 1
    print(indeg)
    q = collections.deque()
    for i in range(n):
        if indeg[i] == 0:
            print(i)
            q.append(i)

    while q:
        print(q, topo)
        node = q.popleft()
        topo.append(node)

        for adjnode in graph[node]:
            indeg[adjnode] -= 1
            if indeg[adjnode] == 0:
                q.append(adjnode)
    return topo
    



if __name__ == "__main__":
    g = Graph(6, True)
    g.from_arr([5, 2, 5, 0, 4, 0, 4, 1, 2, 3, 3, 1])
    ans = [5, 4, 2, 3, 1, 0]
    print(g.graph)
    print(ans, toposort(g.v, g.graph))