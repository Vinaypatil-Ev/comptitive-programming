def sum_equal(arr):
    t = [arr[0]]
    for i in range(1, len(arr)):
        t.append(t[i - 1] + arr[i])
    print(t)


if __name__ == "__main__":
    arr = [7, 3, 4, 0, 7, 8]
    sum_equal(arr)
    