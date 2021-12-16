def find(parent, node):
    if parent[node] == node:
        return node
    if parent[node] != node:
        find(parent[node], parent)

def union(u, v, parent, rank):
    u = find(parent, u)
    v = find(parent, v)

    if u == v:
        return
    if rank[u] >= rank[v]:
        parent[u] = v
    elif rank[v] > rank[v]:
        parent[v] = u
