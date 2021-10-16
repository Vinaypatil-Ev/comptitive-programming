def reverse_and_rotate(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
        
        


if __name__ == "__main__":
    arr = [1, 2, 4, 5, 6, 7, 8, 9]
    print("revesrse")
    reverse_and_rotate(arr, 0, len(arr) - 1)
    print(arr)
    arr = [1, 2, 4, 5, 6, 7, 8, 9]
    print("rotate")
    reverse_and_rotate(arr, 0, 3)
    reverse_and_rotate(arr, 4, len(arr) -1)
    reverse_and_rotate(arr, 0, len(arr) - 1)
    print(arr)