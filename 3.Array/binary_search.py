def binary_search(arr, start, end, e):
    if start < end:
        mid = start + (end - start) // 2
        if arr[mid] == e:
            return mid
        elif arr[mid] > e:
            return binary_search(arr, start, mid, e)
        elif arr[mid] < e:
            return binary_search(arr, mid+1, end, e)
    
arr = [123, 1, 8, 54, 12, 43, 9, 3, 2]
arr.sort()
i = binary_search(arr, 0, len(arr) - 1, 10)
if i:
    print(f"element found at {i}, {arr[i]}")
else:
    print("not found")
