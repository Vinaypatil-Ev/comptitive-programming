def max_product_sub(arr, n):
    maxp = max(arr)
    _max = _min = 1
    for i in arr:
        if i == 0:
            _min = _min = 1
        temp = _max * i
        _max = max(temp, i, i * _min)
        _min = min(_min * i, i, temp)
        maxp = max(_max, maxp)
    return maxp


if __name__ == "__main__":
    # arr = list(map(int, input().strip().split()))
    arr = [8, -2, -2, 0, 8, 0, -6, -8, -6, -1]
    n = len(arr)
    # print(arr)
    x = max_product_sub(arr, n)
    print(x)