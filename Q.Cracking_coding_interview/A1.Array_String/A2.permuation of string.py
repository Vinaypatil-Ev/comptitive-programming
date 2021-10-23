def swap(s, x, y):
    s[x], s[y] = s[y], s[x]
def gp(s, left, right):
    if left < right:
        for i in range(left, right+1):
            swap(s, left, i)
            # yield from gp(s, left+1, right)
            gp(s, left+1, right)
            swap(s, left, i)
    if left == right:
        # yield "".join(s)
        print("".join(s))


if __name__ == "__main__":
    s = "abc"
    s = list(s)
    # x = iter(gp(s, 0, len(s) - 1))
    # for i in range(4):
        # print(next(x))
    gp(s, 0, len(s) - 1)