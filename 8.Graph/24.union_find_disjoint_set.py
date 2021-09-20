inputLine = lambda: list(map(int, input().split()))
def union(parent, a, b):
    ap = find(parent, a)
    bp = find(parent, b)
    if ap == bp:
        return True
    return False

def union_op(parent, a, b, rank):
    ap = find(parent, a)
    bp = find(parent, b)
    
    if rank[ap] > rank[bp]:
        parent[bp] = ap
    elif rank[ap] < rank[bp]:
        parent[ap] = bp
    else:
        parent[ap] = bp
        rank[bp] += 1
    

def union(parent, a, b):
    ap = find(parent, a)
    bp = find(parent, b)
    if ap == bp:
        return True
    return False

# def find(parent, v):
#     if parent[v] == -1:
#         return v
#     return find(parent, parent[v])


def find(parent, v):
    if parent[v] == -1:
        return v
    u = find(parent, parent[v])
    parent[v] = u
    return u


if __name__ == "__main__":
    v, e = inputLine()
    parent = [-1] * v
    rank = [0] * v
    for _ in range(e):
        a, b = inputLine()
        parent[b-1] = a-1
    op, c = inputLine()
    if op == -1:
        for _ in range(c):
            a, b = inputLine()
            print(union(parent, a-1, b-1))
    elif op == -2:
        for _ in range(c):
            f = int(input())
            print(find(parent, f-1) + 1)