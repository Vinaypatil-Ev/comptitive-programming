inputLine = lambda: list(map(int, input().split()))

def is_eq(res, v):
    res[0] += v[0]
    res[1] += v[1]
    res[2] += v[2]

if __name__ == "__main__":
    res = [0, 0, 0]
    n = int(input())
    for _ in range(n):
        is_eq(res, inputLine())
    
    print("YES" if res[0] == res[1] == res[2] == 0 else "NO")