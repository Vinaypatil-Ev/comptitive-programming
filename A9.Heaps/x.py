import heapq as h


arr = ["3","6","7","10"]
heap = []
for i in arr:
    h.heappush(heap, (int(i), i))
x = None
for i in range(len(arr) - 2 + 1):
    x = h.heappop(heap)
print(x)