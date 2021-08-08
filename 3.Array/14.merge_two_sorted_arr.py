# first approach
# create third array
def merge_array(arr1, arr2, n, m):
    arr3 = [None] * (n + m)
    i = 0
    j = 0
    k = 0
    while i < n and j < m:
        if arr1[i] < arr2[j]:
            arr3[k] = arr1[i]
            i += 1
            k += 1
        else:
            arr3[k] = arr2[j]
            j += 1
            k += 1

    while i < n:
        arr3[k] = arr1[i]
        i += 1
        k += 1

    while j < m:
        arr3[k] = arr2[j]
        j += 1
        k += 1
    return arr3


def merge_arr_2(arr1, arr2, n, m):
    i = m - 1
    while i >= 0:
        last = arr1[n - 1]
        j = n - 2
        while j >= 0 and arr1[j] > arr2[i]:
            arr1[j + 1] = arr1[j]
            j -= 1
        if j != n - 2 or last > arr2[i]:
            arr1[j + 1] = arr2[i]
            arr2[i] = last
        i -= 1
# O(n*m)

def merge_arr_3(arr1, arr2, n, m):
    i = j = 0
    k = m - 1
    while i <= k and j < m:
        if arr1[i] < arr2[j]:
            i += 1
        else:
            arr2[j], arr1[k] = arr1[k], arr2[j]
            j += 1
            k -= 1

    print(arr1)
    print(arr2)
    arr1.sort()
    arr2.sort()
    print(arr1)
    print(arr2)


if __name__ == "__main__":
    # arr1 = [0, 1, 5, 7]
    # arr2 = [2, 4, 6, 8, 9]
    # x = merge_array(arr1, arr2, len(arr1), len(arr2))
    # print(x)
    # arr1 = [1, 2, 6, 7, 8, 9]
    # arr2 = [0, 3, 5]
    arr1 = [1, 3, 5, 7]
    arr2 = [0, 2, 6, 8, 9]
    merge_arr_2(arr1, arr2, len(arr1), len(arr2))
    print("--")
    print(arr1)
    print(arr2)
    print("---")
    # arr1 = [1, 2, 5, 10, 11, 15, 20]
    # arr2 = [0, 3, 6, 8, 9]
    # merge_arr_3(arr1, arr2, len(arr1), len(arr2))
    