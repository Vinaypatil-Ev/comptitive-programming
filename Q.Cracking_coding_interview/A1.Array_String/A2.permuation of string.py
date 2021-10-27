def swap(s, x, y):
    s[x], s[y] = s[y], s[x]

def gp(s, left, right):
    if left < right:
        for i in range(left, right):
            swap(s, left, i)
            gp(s, left+1, right)
            swap(s, left, i)
    if left == right:
        print("".join(s))

def gp_yield(s, left, right):
    if left < right:
        for i in range(left, right):
            swap(s, left, i)
            yield from gp(s, left+1, right)
            swap(s, left, i)
    if left == right:
        yield "".join(s)

def gp_arr(n, k, sub:set):
    if len(sub) == n:
        yield sub
        # yield "".join(sub)
        # print()
        # return
    for i in range(1, n):
        if str(i) in sub:
            continue
        # sub.add(str(i+1))
        sub = sub + str(i)
        yield from gp_arr(n, k, sub)
        # sub.remove(str(i+1))
        sub = sub[:-1]

if __name__ == "__main__":
    # s = "123456789"
    # s = list(s)
    # gp(s, 0, len(s) - 1)

    # x = iter(gp_yield(s, 0, len(s)))
    # for i in range(800):
    #     print(next(x), i), 
    n, k = 9, 100
    # n = int(input())
    # k = int(input())
    x = iter(gp_arr(n, k, ""))
    ans = ""
    for i in range(k):
        print(next(x))