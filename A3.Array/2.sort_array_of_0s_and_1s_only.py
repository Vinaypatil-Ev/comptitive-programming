def swap(arr, x, y):
    arr[x], arr[y] = arr[y], arr[x]


def sort_01(low, high, arr):
    while low <= high:
        if arr[low] == 0:
            low += 1
        else:
            swap(arr, low, high)
            high -= 1


if __name__ == "__main__":
    arr = [1, 0, 1, 0, 1, 0, 1, 0, 0]
    sort_01(0, len(arr) - 1, arr)
    print(arr)