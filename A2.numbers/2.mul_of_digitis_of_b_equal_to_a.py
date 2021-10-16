def find(a):
    mul = []
    for i in range(9, 1, -1):
        while a % i == 0:
            a /= i
            mul.append(i)
    if mul:
        mul.sort()
        b = 0
        for i in mul:
            b = b * 10 + i
        return b
    else:
        return "Not Possible"



if __name__ == "__main__":
    a = [10, 56, 150, 13]
    b = [25, 78, 556, "Not Possible"]
    for i in range(len(a)):
        out = find(a[i])
        if out != b[i]:
            print(f"Wrong: {a[i]}, -> {out} expected: {b[i]}")
            continue
        print(f"Correct: {a[i]}, {out}")
        