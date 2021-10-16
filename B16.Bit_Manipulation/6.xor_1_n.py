# brut force approach
def xor1n(n):
    r = 0
    i = 1
    while i <= n:
        r ^= i
        i += 1
    return r
    
    
def xor1ne(n):
    r = n % 4
    if r == 0:
        return n
    if r == 1:
        return 1
    if r == 2:
        return n + 1
    if r == 3:
        return 0


if __name__ == "__main__":
    n = int(input())
    print(xor1n(n))
    print(xor1ne(n))