def smallet_sum(arr):
    s = float("inf")
    a = s
    for i in arr:
        if a > 0:
            a = i
            print("a ", i)
        else:
            a += i
            print("+a ", i)
        s = min(a, s)
    return s


if __name__ == "__main__":
    arr = [3, -4, 2, -3, -1, 7, -5]
    x = smallet_sum(arr)
    print("smallest sum is ", x)