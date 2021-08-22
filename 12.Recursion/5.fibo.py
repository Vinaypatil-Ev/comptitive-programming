from timeit import timeit
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
    n  = 15
    # x = fibo(n)
    print((timeit(lambda: fibo(n))), "time")
    x = fiboi(n)
    print(f"fibo of {n} is {x}")