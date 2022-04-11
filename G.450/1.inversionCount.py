# def merge(arr, left, mid, right):
#     n = mid - left + 1
#     m = right - mid
#     leftArr = [arr[left + i] for i in range(n)]
#     rightArr = [arr[mid + i + 1] for i in range(m)]
#     i = j = 0
#     k = left
#     count = 0
#     while i < n and j < m:
#         if leftArr[i] <= rightArr[j]:
#             arr[k] = leftArr[i]
#             i += 1
#             k += 1
#         else:
#             arr[k] = rightArr[j]
#             j += 1
#             k += 1
#             count += n - i
#     while i < n:
#         arr[k] = leftArr[i]
#         i += 1
#         k += 1
#     while j < m:
#         arr[k] = rightArr[j]
#         j += 1
#         k += 1
    
#     return count
def merge(arr, left, mid, right):
    n = mid - left + 1
    m = right - mid
    leftArr = [arr[left + i] for i in range(n)]
    rightArr = [arr[mid + i + 1] for i in range(m)]
    i = j = 0
    k = left
    count = 0
    while i < n and j < m:
        if leftArr[i] <= rightArr[j]:
            arr[k] = leftArr[i]
            i += 1
            k += 1
        else:
            arr[k] = rightArr[j]
            j += 1
            k += 1
            count += n - i
    while i < n:
        arr[k] = leftArr[i]
        i += 1
        k += 1
    while j < m:
        arr[k] = rightArr[j]
        j += 1
        k += 1
    
    return count
def mergecount(arr, left, right):
    count = 0
    if left < right:
        mid = left + (right - left) // 2
        count += mergecount(arr, left, mid)
        count += mergecount(arr, mid + 1, right)
        count += merge(arr, left, mid, right)
    return count
def inversionCount(arr, n):
    return mergecount(arr, 0, n - 1)


if __name__ == "__main__":
    arr = list(map(int, input().split()))
    print(inversionCount(arr, len(arr)))