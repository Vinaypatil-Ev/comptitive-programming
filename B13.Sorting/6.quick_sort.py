def quick_sort(arr, n, left, right):
    if left < right:
        p = partition(arr, n, left, right)
        quick_sort(arr, n, left, p - 1)
        quick_sort(arr, n, p + 1, right)

def partition(arr, n, left, right):
    pivot = arr[left]
    pivot_i = left
    while left < right:
        while left < n and arr[left] <= pivot:
            left += 1
        while arr[right] > pivot:
            right -= 1
        if left < right:
            swap(arr, left, right)
    swap(arr, right, pivot_i)
    return right

def swap(arr, left, right):
    arr[left], arr[right] = arr[right], arr[left]

if __name__ == "__main__":
    arr = [18, 16, 2, 4, 6, 8, 1, 12, 0]
    quick_sort(arr, len(arr), 0, len(arr) - 1)
    print(arr)