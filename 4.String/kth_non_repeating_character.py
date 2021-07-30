s = "goldminesgoldes"
k = 3
t = 0
# for i in s:
#     if s.count(i) == 1:
#         t += 1
#     if t == k:
#         print(i)
#         break

map = {}
for i in s:
    if i in map:
        map[i] += 1
    if i not in map:
        map[i] = 1
count = 0
for key, v in map.items():
    if v == 1:
        count += 1
    if count == 3:
        print(key)
        break
        
    