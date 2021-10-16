def permute(s, left, right, count = 0):
    if left < right:
        for i in range(left, right + 1):
            swap(s, left, i)
            count = permute(s, left + 1, right, count=count)
            swap(s, i, left)
    elif left == right:
        count += 1
        print("".join(s))
    return count

def swap(s: str, x, y):
    s[x], s[y] = s[y], s[x]
    

# time to print on permutio * no of permutation
# level = len(s) = n
# n * n!
if __name__ == "__main__":
    s = "abc"
    s = list(s)
    x = permute(s, 0, len(s) - 1)
    print(x)
