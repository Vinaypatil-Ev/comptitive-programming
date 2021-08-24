def traverse(arr, left, top, row, col):
    print(left, top)
    if left == col - 1 and top == row - 1:
        print("hi")
        return
    if left > col or left < 0:
        print("hi2")
        return
    if top > row or top < 0:
        print("hi3")
        return
    print(arr[left][top], end=" ")
    traverse(arr, left - 1, top, row, col) 
    traverse(arr, left, top - 1, row, col) 
    traverse(arr, left + 1, top, row, col) 
    traverse(arr, left, top + 1, row, col)
    return
    



if __name__ == "__main__":
    arr = [
        [1, 2, 3, 4],
        [19, 192, 29, 2],
        [93, 32, 34, 5],
        [12, 43, 4, 6],
        ]
    row = len(arr)
    col = len(arr[0])
    traverse(arr, 0, 0, row, col)