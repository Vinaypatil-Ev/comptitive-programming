def dfs(arr, n, size):
    # print(size, n)
    if size == 0:
        return 0
    if n == 0:
        return float("inf")
    if arr[n - 1] > size:
        return dfs(arr, n - 1, size)
    else:
        return min(1 + dfs(arr, n, size - arr[n - 1]), dfs(arr, n - 1, size))

    





arr = [1, 3, 5, 7, 10]
size = 72
n = len(arr)
count = dfs(arr, n, size)
print(count)






















# a = input()
# if a == "":
#     print(a)
# s = a[:2]
# new = a.replace(s, "$")
# n = len(new)
# count = 1
# for i in range(1, n):
#     if new[i] == "$" and new[i - 1] != "$":
#         count += 1
# print(count)