def swap(arr, x, y):
    arr[x], arr[y] = arr[y], arr[x]

def move_neg(arr, n):
    low = 0
    high = n - 1
    while low <= high:
        if arr[low] >= 0:
            low += 1
        else:
            swap(arr, low, high)
            high -= 1

if __name__ == "__main__":
    arr = [0, -1, 2, -5, -9, 2, -3, 2, -3]
    move_neg(arr, len(arr))
    print(arr)