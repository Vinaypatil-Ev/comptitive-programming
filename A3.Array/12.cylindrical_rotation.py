# write a program to cylindrically rotate an arrray by 1
def rotate_right_by_one(arr):
    n = len(arr)
    temp = arr[n - 1]
    for i in range(n-1, 0, -1):
        arr[i] = arr[i - 1]
    arr[0] = temp
    print(arr)

def rotate_left_by_one(arr):
    n = len(arr)
    temp = arr[0]
    for i in range(1, n):
        arr[i - 1] = arr[i]
    arr[n - 1] = temp
    print(arr)
    
    
    
if __name__ == "__main__":
    print([1, 2, 3, 4, 5])
    rotate_right_by_one([1, 2, 3, 4, 5])
    rotate_left_by_one([1, 2, 3, 4, 5])
    