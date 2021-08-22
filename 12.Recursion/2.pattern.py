def ppattern(n):
    if n >= 0:
        for _ in range(n):
            print("*", end=" ")
        print()
        ppattern(n - 1)
def ppattern2(n):
    if n >= 0:
        ppattern2(n - 1)
        for _ in range(n):
            print("*", end=" ")
        print()

if __name__ == "__main__":
    ppattern(6)
    ppattern2(6)