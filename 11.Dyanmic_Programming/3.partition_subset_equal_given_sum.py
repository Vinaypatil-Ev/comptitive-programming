def partion_subset(arr, s, n, d):
    if s == 0:
        return True
    elif n < 0 or s < 0:
        return False
    if (s, n) not in d:
        d[(s, n)] = partion_subset(arr, s, n - 1, d) or partion_subset(arr, s - arr[n - 1], n - 1, d)
    return d[(s, n)]
def check_partition(arr, s, n):
    asum = sum(arr)
    if asum & 1:
        return False
    d = {}
    return partion_subset(arr, s, n, d)


if __name__ == "__main__":
    arr = [3, 5, 3, 11]
    s = 11
    n = len(arr)
    x = check_partition(arr, s, n)
    if x:
        print("possibe")
    else:
        print("Not possible")