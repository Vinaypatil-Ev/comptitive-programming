def b_sort(arr, n):
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                
def b_sort_r(arr, n):
    if n >= 0:
        for j in range(n - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        b_sort_r(arr, n - 1)
        



if __name__ == "__main__":
    arr = [10, 3, 5, 12, 0, 14, 1, 8]
    b_sort(arr, len(arr))
    print(arr)
    arr2 = [11, 9, 0, 42, 1, 67, 4]
    b_sort_r(arr2, len(arr) - 1)
    print(arr2)
    