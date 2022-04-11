import collections
def is_valid(board):
    col = collections.defaultdict(set)
    row = collections.defaultdict(set)
    box = collections.defaultdict(set)
    n = len(board)
    m = len(board[0])
    for i in range(n):
        for j in range(m):
            if board[i][j] in col[j] or \
                board[i][j] in row[i] or \
                board[i][j] in box[(i // 3, j // 3)]:
                return False
            row[i].add(board[i][j])
            col[j].add(board[i][j])
            box[(i // 3, j // 3)].add(board[i][j])
    return True
        
if __name__ == "__main__":
    for i in range(int(input())):
        arr = []
        N = int(input())
        for _ in range(9):
            row = list(map(str, input().split()))
            arr.append(row)
        print(f"Case #{i + 1}: Yes" if is_valid(arr) else f"Case #{i + 1}: No")
