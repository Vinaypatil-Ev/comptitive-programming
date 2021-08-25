import heapq as h


arr = [1, 3, 4, 5, 6, 7]
arr = list(map(lambda x: -x, arr))
h.heapify(arr)

print(arr)