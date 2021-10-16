import math
def segment_sieve(n):
    lim = int(math.sqrt(n))
    mark = [False] * (lim + 1)
    primes = []
    i = 2
    while i * i <= n:
        if not mark[i]:
            j = i * i
            primes.append(i)
            while j <= n:
                mark[i] = True
                j += i
        i += 1
    is_prime = [True] * (n + 1) 
    for i in primes:
        j = i * i
        while j <= n:
            is_prime[j] = False
            j += i
    return is_prime

def segment_range_sieve(l, r):
    lim = int(math.sqrt(r))
    is_prime_lim = [False] * (lim + 1)
    primes = []
    for i in range(2, lim+1):
        if not is_prime_lim[i]:
            primes.append(i)
            for j in range(i * i, lim + 1, i):
                is_prime_lim[j] = True
    
    is_prime = [True] * (r - l + 1)
    for i in primes:
        j = max(i * i, l + i -1)
        while j <= r:
            is_prime[j - l] = False
            j += i
    if l == 1:
        is_prime[0] = False
    return is_prime
    

if __name__ == "__main__":
    n = 30
    p = segment_sieve(n)
    for i in range(len(p)):
        if p[i]:
            print(i, end=" ")
    # print(get_range(30))
    print()
    p = segment_range_sieve(1, 20)
    for i in range(len(p)):
        if p[i]:
            print(i, end=" ")
    print()
    print(p)
