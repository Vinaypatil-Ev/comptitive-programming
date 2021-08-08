def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n - 2)

#dynamic programming
d = {0:0, 1:1}
def fib2(n):
    if n not in d:
        d[n] = fib2(n-1) + fib2(n-2)
    return d[n]


if __name__ == "__main__":
    print(fib(10))
    print(fib2(10))