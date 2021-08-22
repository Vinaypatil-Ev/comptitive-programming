from typing import List, NewType


def rotate(matrix: List):
    row = len(matrix)
    col = len(matrix[0])
    new_mat = [[0] * col for _ in range(row)]
    n = 0
    for i in range(row):
        m = col - 1
        for j in range(col):
            new_mat[i][j] = matrix[m][n]
            m -= 1
        n += 1
    return new_mat

def rotatei(matrix: List):
    row = len(matrix)
    col = len(matrix[0])
    new_marix.copy()
    # n = 0
    # for i in range(row):
    #     m = col - 1
    #     for j in range(col):
    #         matrix[i][j] = new_mat[m][n]
    #         m -= 1
    #     n += 1


if __name__ == "__main__":
    # mat = [
    #     [4, 6, 9, 12],
    #     [3, 6, 9, 12],
    #     [2, 5, 8, 11],
    #     [1, 4, 7, 10]
    # ]
    mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    r = [[7,4,1],[8,5,2],[9,6,3]]
    
    # matrix = rotate(mat)
    rotatei(mat)
    print(mat)
    print(mat == r)