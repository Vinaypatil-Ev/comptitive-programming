def traping_water(arr, n):
    low = 0
    high = n - 1
    maxarea = 0
    while low < high:
        if arr[low] < arr[high]:
            l = min(arr[low], arr[high])
            area = (high - low) * l
            maxarea = max(area, maxarea)
            low += 1
        else:
            l = min(arr[low], arr[high])
            area = (high - low) * l
            maxarea = max(area, maxarea)
            high -= 1
    return maxarea



if __name__ == "__main__":
    arr1 = [1, 3, 2, 0, 5, 2, 5, 4, 1, 2]
    x = traping_water(arr1, len(arr1))
    print("max area: ", x)
    arr1 = [2, 3, 5, 1, 0, 3, 1, 4, 1, 2]
    x = traping_water(arr1, len(arr1))
    print("max area: ", x)
            