def max_and_min(arr):
    min = max = arr[0]
    for i in arr:
        if i < min:
            min = i
        if i > max:
            max = i
    return min, max

# touranament approach
def max_and_min2(low, high, arr):
    if low == high:
        return arr[low], arr[low]
    elif high == low + 1:
        return (arr[0], arr[1]) if arr[0] < arr[1] else (arr[1], arr[0])
    else:
        mid = (high + low) // 2
        min1, max1 = max_and_min2(0, mid, arr)
        min2, max2 = max_and_min2(mid+1, high, arr)
        return min(min1, min2), max(max1, max2)

if __name__ == "__main__":
    arr = [6, 33, 8, 99, 1, 3, 90, 100]
    # arr = [244, 199]
    # min, max = max_and_min(arr)
    min, max = max_and_min2(0, len(arr) - 1, arr)
    print(f"max: {max}, min: {min}")