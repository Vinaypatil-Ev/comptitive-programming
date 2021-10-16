def sort_arr(arr):
    left = mid = 0
    right = len(arr) - 1
    while mid < right:
        if arr[mid] == 0:
            arr[mid], arr[left] = arr[left], arr[mid]
            left += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        elif arr[mid] == 2:
            arr[mid], arr[right] = arr[right], arr[mid]
            right -= 1

if __name__ == "__main__":
    arr = [0, 1, 2, 1, 0, 1, 2, 1, 1, 2, 2, 0]
    sort_arr(arr)
    print(arr)