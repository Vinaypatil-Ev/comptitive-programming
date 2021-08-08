def subset(arr, s, n, d):
    if s == 0:
        return 1
    if n == 0 and s != 0:
        return 0
    if arr[n - 1] > s:
        return subset(arr, s, n - 1, d)
    return subset(arr, s - arr[n - 1], n - 1, d) + subset(arr, s, n - 1, d)

def subset2(arr, s, n, d):
    if s == 0:
        return 1
    if n == 0 and s != 0:
        return 0
    if s not in d:
        if arr[n - 1] > s:
            d[s] = subset(arr, s, n - 1, d)
        else:
            d[s] = subset(arr, s - arr[n - 1], n - 1, d) + subset(arr, s, n - 1, d)
    return d[s]

if __name__ == "__main__":
    nums = [3,5,6,4]
    target = 9
    n = len(nums)
    d = {}
    # count = subset(nums, target, n, d)
    count = subset2(nums, target, n, d)
    print(f"There are {count} subsets")
    print(d)