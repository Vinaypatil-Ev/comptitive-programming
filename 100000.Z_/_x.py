def max_count(no):
    d = {}
    for i in no:
        if i & 1:
            if i in d:
                d[i] += 1
            elif i not in d:
                d[i] = 1
    m = 0
    odd = 0
    for k, v in d.items():
        if m < v:
            odd = k
            m = v
    return odd


no = list(map(int, input().split()))
x = max_count(no)
print(x)