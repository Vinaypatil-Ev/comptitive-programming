def spiral_matrix_read(arr, row, column):
    left = 0
    right = column - 1
    top = 0
    bot = row - 1
    while top <= bot and left <= right:
        for i in range(left, right + 1):
            print(arr[top][i], end=" ")
        top += 1
        for i in range(top, bot + 1):
             print(arr[i][right], end=" ")
        right -= 1
        if top < bot:
            for i in range(right, left-1, -1):
                print(arr[bot][i], end=" ")
            bot -= 1
        if left < right:
            for i in range(bot, top-1, -1):
                print(arr[i][left], end=" ")
            left += 1

def spiralPrint(m, n, a):
    k = 0
    l = 0
    m = m - 1
    n = n - 1
 
    ''' k - starting row index
        m - ending row index
        l - starting column index
        n - ending column index
        i - iterator '''
 
    while (k < m+1 and l < n+1):
 
        # Print the first row from
        # the remaining rows
        for i in range(l, n+1):
            print(a[k][i], end=" ")
 
        k += 1
 
        # Print the last column from
        # the remaining columns
        for i in range(k, m+1):
            print(a[i][n], end=" ")
 
        n -= 1
 
        # Print the last row from
        # the remaining rows
        if (k < m):
 
            for i in range(n, (l - 1), -1):
                print(a[m][i], end=" ")
 
            m -= 1
 
        # Print the first column from
        # the remaining columns
        if (l < n):
            for i in range(m, k - 1, -1):
                print(a[i][l], end=" ")
 
            l += 1

if __name__ == "__main__":
    arr = [[2,5,8],[4,0,-1]]
    # [
    #         [1, 2, 3],
    #         [8, 9, 4],
    #         [7, 6, 5], 
    #     ]
    r = 3
    c = 3
    spiral_matrix_read(arr, 2, 3)
    print()
    spiralPrint(2, 3, arr)
    """
    [
        [1, 2, 3], [0, 1, 2], 
        [8, 9, 4], [1, 11, 12],
        [7, 6, 5], [2, 21, 22],
    ]
    """