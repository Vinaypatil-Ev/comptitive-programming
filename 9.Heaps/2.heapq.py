import heapq as h


l1 = [10, 1, 3, 5, 2, 4]
l2 = [(1, 100), (5, 101), (2, 143), (3, 500)]
h.heapify(l1)

# for i in range(6):
#     print(h.heappop(l1))
    
# h.heappush(l1, 1000)
# print(l1)

# h.heappushpop(l1, 50)
# print(l1)

h.heapify(l2)
h.heappush(l2, (40, 800))
print(l2)
for i in range(len(l2)):
    print(h.heappop(l2))
