def subset(arr, n):
    mask = 0
    all_set = set()
    while mask < (1 << n):
        sub = []
        for i in range(n):
            if mask & (1 << i):
                sub.append(arr[i])
        sub.sort()
        all_set.add(tuple(sub))
        mask += 1
    return sorted(all_set)


if __name__ == "__main__":
    arr = [2, 1, 2]
    x = subset(arr, len(arr))
    print(x)