def bawl_sum(arr):
    x = arr[0]
    y = arr[len(arr) - 1]
    mid = len(arr) // 2
    c = x + y - arr[mid]
    return c

print(bawl_sum([1, 3, 5, 9, 11]))
print(bawl_sum([2, 4, 6, 10, 12]))