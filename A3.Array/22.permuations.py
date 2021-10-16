def permute(arr, left, right, count=0, s=set()):
    if left < right:
        for i in range(left, right + 1):
            swap(arr, left, i)
            permute(arr, left + 1, right, count, s)
            swap(arr, i, left)
    elif left == right:
        s.add(tuple(arr))
    return s

def swap(s: str, x, y):
    s[x], s[y] = s[y], s[x]
    

# time to print on permutio * no of permutation
# level = len(s) = n
# n * n!
if __name__ == "__main__":
    s = [1, 2, 3]
    x = permute(s, 0, len(s) - 1)
    print([[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]])
    print(x)
