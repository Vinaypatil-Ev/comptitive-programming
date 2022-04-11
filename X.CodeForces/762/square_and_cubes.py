def find(n):
    arr = set()
    arr.add(1)
    i = 2
    while i ** 3 <= n:
        arr.add(i ** 3)
        arr.add(i ** 2)
        i += 1
    while i ** 2 <= n:
        arr.add(i ** 2)
        i += 1
    return len(arr)


if __name__ == "__main__":
    t = int(input())
    while t:
        print(find(int(input())))
        t -= 1
