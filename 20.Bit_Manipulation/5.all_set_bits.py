def all_set(n):
    while n:
        if not n & 1:
            return 0
        n >>= 1
    return 1



if __name__ == "__main__":
    n = int(input())
    print(all_set(n))