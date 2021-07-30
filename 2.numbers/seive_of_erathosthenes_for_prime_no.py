def seive(n):
    d = [True for i in range(n+1)]
    p = 2
    while p ** 2 <= n:
        if d[p]:
            for i in range(p * p, n+1, p):
                d[i] = False
        p += 1
    for i in range(len(d)):
        if d[i]:
            print(i, end=" ")

seive(30)      
    
    