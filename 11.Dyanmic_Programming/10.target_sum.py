def target_sum(arr, size, n, d):
    if n == 0:
        return 0
    if size == 0:
        return 1
    if (size, n) not in d:
        if arr[n] > size:
            d[(size, n)] = target_sum(arr, size, n - 1, d)
        else:
            d[(size, n)] = target_sum(arr, size, n - 1, d) + 1 + target_sum(arr, size - arr[n], n - 1, d) 
    return d[(size, n)]


if __name__ == "__main__":
    d = dict()
    arr = [1,1,1,1,1]
    n = len(arr)
    target = 3
    new_target = (sum(arr) + target) // 2
    print(new_target)
    z = target_sum(arr, new_target, n - 1, d)
    print(z)