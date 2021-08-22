def b_sort(arr, n):
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    
if __name__ == "__main__":
    arr = [10, 3, 5, 12, 0, 14, 1, 8]
    b_sort(arr, len(arr))
    print(arr)
    