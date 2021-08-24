import time
def fibo(n):
    if n == 1 or n == 2:
        return 1
    return fibo(n - 1) + fibo(n - 2)


def fiboi(n):
    a = 1
    b = 1
    c = 0
    if n == 1 or n == 2:
        return 1
    for _ in range(3, n+1):
        c = a + b
        a = b
        b = c
    return c


if __name__ == "__main__":
    n  = 20
    # x = fibo(n)
    s1 = time.time()
    fiboi(n)
    s2 = time.time()
    print(f"iterative time for fibo of {n}: {(s2 - s1)*1000}")
    s3 = time.time()
    fibo(n)
    s4 = time.time()
    print(f"recurse time for fibo of {n}: {(s4 - s3)*1000}")
    # x = fiboi(n)
    # print(f"fibo of {n} is {x}")