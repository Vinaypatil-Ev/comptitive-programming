def add(a, b):
    c = a & b
    r = a ^ b
    while c:
        shift = c << 1
        c = r & shift
        r ^= shift
    return r




if __name__ == "__main__":
    a, b = list(map(int, input().split()))
    x = add(a, b)
    print(x)