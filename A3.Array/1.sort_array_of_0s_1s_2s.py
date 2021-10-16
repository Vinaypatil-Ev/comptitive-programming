def swap(arr, x, y):
    arr[x], arr[y] = arr[y], arr[x]

def count(arr):
    d = {}
    for i in arr:
        if i in d:
            d[i] += 1
        if i not in d:
            d[i] = 1
    return d

def sort_012_1(arr):
    d = count(arr)
    zero = d[0]
    one = d[1]
    two = d[2]
    arr2 = []
    for i in range(zero):
        arr2.append(0)
    for i in range(one):
        arr2.append(1)
    for i in range(two):
        arr2.append(2)
    return arr2

# doutch national flag algorithm
def sort_012_2(arr):
    mid = low = 0
    high = len(arr) - 1
    while mid <= high:
        if arr[mid] == 0:
            swap(arr, low, mid)
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            swap(arr, mid, high)
            high -= 1
    

if __name__ == "__main__":
    arr = [0, 1, 2, 2, 1, 0, 0, 2, 0, 1, 1, 0]
    # arr = sort_012_1(arr)
    # print(arr)
    sort_012_2(arr)
    print(arr)
                
    
