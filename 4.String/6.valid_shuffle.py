def check_is_shuffle(s, a, b):
    if len(a + b) != len(s):
        return False
    s = sorted(s)
    a = sorted(a)
    b = sorted(b)
    sn = len(s)
    an = len(a)
    bn = len(b)
    i = k = j = 0
    while k < sn:
        if i < an and s[k] == a[i]:
            i += 1
        if j < bn and s[k] == a[j]:
            j += 1
        k += 1
    if i == an and j == bn:
        return True
    else:
        return False            



if __name__ == "__main__":
    s1 = "XY"
    s2 = "12"
    s = "Y12XX"
    if check_is_shuffle(s, s1, s2):
        print("is shuffled")
    else:
        print("invalid shuffle")