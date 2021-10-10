def cc(n, m):
    if n == 0 or m == 0 or n == m:
        return 1
    x = cc(n - 1, m)
    y = cc(n - 1, m - 1)
    print(x, y, end=" ")
    return x + y


if __name__ == "__main__":
    print(cc(4, 5))