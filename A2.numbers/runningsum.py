# def minStart(arr):
#     startValue = 0
#     for x in range(startValue, 999999):
#         s = x
#         for n in arr:
#             s += n
#             if s < 1:
#                 break
#         if s >= 1:
#             return x
#     return 0


def minStart(arr):
    x = 1
    for i in range(len(arr) - 1, -1, -1):
        x = x - arr[i]
        if x < 1:
            x = 1
    return x


print(minStart([-5, 4, -2, 3, 1]))
print(minStart([-5, 4, -2, 3, 1]))