def prefix_sum(arr, n):
    pre = 0
    for i in range(n):
        pre += arr[i]
        arr[i] = pre

def prefix_sum_2D(arr, r, c):
    for i in range(1, c):
        arr[0][i] = arr[0][i-1] + arr[0][i]
    for i in range(1, r):
        arr[i][0] = arr[i-1][0] + arr[i][0]
    for i in range(1, r):
        for j in range(1, c):
            arr[i][j] = arr[i-1][j] + arr[i][j-1] - arr[i-1][j-1] + arr[i][j]

if __name__ == "__main__":
    # arr = [10, 20, 10, 5, 15]
    # prefix_sum(arr, len(arr))
    # print(arr)
    
    arr_2d = [
                [10, 20, 30],
                [5, 10, 20],
                [2, 4, 6]
              ]
    prefix_sum_2D(arr_2d, 3, 3)
    for i in arr_2d:
        print(*i)
    