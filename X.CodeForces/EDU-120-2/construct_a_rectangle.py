inputLine = lambda: list(map(int, input().split()))
def find(a, b, c):
    return (a + b + c) % 2 == 0

            



if __name__ == "__main__":
    t = int(input())
    while t:
        print("YES" if find(*`inputLine()) else "NO")
        t -= 1