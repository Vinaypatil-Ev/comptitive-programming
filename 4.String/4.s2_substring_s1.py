def is_sub(s, sub):
    n = len(s)
    for i in range(n):
        t = ""
        for j in range(i, n):
            t += s[j]
            if t == sub:
                return True
    return False

def is_sub2(s, sub):
    n = len(s)
    m = len(sub)
    left = 0
    right = 0
    right2 = m - 1
    while left < n:
        if right == m - 1:
            return True
        print(s[left], sub[right], s[left + right2], sub[right2], right, right2)
        if s[left] == sub[right] and s[left + right2] == sub[right2]:
            right += 1
            right2 -= 1
        else:
            right = 0
            right2 = m - 1
        left += 1
    return False



if __name__ == "__main__":
    s = "imthebossornot"
    sub1 = "sor"
    sub2 = "sort"
    x = "is" if is_sub2(s, sub1) else "is not"
    print(f"{sub1} {x} substring of {s}")
    x = "is" if is_sub2(s, sub2) else "is not"
    print(f"{sub2} {x} substring of {s}")
