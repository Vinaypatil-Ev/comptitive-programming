def is_square(s):
    n = len(s)
    if n & 1:
        return False
    return s[:n//2] == s[n//2:]




if __name__ == "__main__":
    t = int(input())
    while t:
        print("YES" if is_square(input().strip()) else "NO")
        t -= 1