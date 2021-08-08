# union and intersection of two sorted arrays

def form_map(arr, d):
    for i in arr:
        if i in d:
            d[i] += 1
        if i not in d:
            d[i] = 1
def union_and_inter(a, b):
    d = {}
    form_map(a, d)
    form_map(b, d)
    return [k for k in d.keys()], [k for k, v in d.items() if v > 1]


if __name__ == "__main__":
    a = [1, 2, 3, 4, 5]
    b = [1, 2, 3]
    u, i = union_and_inter(a, b)
    print(f"union {u} \nintersection: {i}")