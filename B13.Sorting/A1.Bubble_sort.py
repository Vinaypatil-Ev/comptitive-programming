def bubble_sort(arr):
    for _ in range(len(arr)):
        for j in range(1, len(arr)):
            if arr[j - 1] > arr[j]:
                arr[j - 1], arr[j] = arr[j], arr[j - 1]



if __name__ == "__main__":
    arr = [19, 4, 18, 1, 25, 2, 4, 8]
    bubble_sort(arr)
    print(arr)
