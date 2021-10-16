def fact(n):
    if n < 2:
        return 1
    return n * fact(n - 1)

# iterative version
def facti(n):
    f = 1
    for i in range(2, n + 1):
        f *= i
    return f



if __name__ == "__main__":
    n = 5
    x = fact(n)
    # x = facti(n)
    print(f"factorial of {n} is {x}")