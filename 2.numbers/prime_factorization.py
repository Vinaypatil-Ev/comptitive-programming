def prime_factors(n):
    while n % 2 == 0:
        print(2)
        n = n // 2
    
    i = 3
    while i * i <= n:
        while n % i == 0:
            print(i)
            n = n // i
        i += 2
    
    if n > 2:
        print(n)
        
if __name__ == "__main__":
    n = 765478
    prime_factors(n)