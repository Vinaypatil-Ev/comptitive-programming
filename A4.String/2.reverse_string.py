def reverse_string(s):
    s = list(s)
    t = ""
    while s:
        t += s.pop()
    return t

if __name__ == "__main__":
    s = "goldminestelifilm"
    x = reverse_string(s)
    print(x)