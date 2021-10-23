def swap(s, x, y):
    s[x], s[y] = s[y], s[x]

def generate_permuation(s, left, right):
    if left < right:
        for i in range(left, right+1):
            swap(s, left, i)
            generate_permuation(s, left+1, right)
            swap(s, left, i)
    if left == right:
        print("".join(s))


if __name__ == "__main__":
    s = "abc"
    s = list(s)
    generate_permuation(s, 0, len(s) - 1)