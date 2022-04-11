def repeatedSubstringPattern(str):
        if not str:
            return False
        ss = (str + str)[1:-1]
        if ss.find(str) == -1:
            return ""
        mx = str[0]
        for i in range(1, len(s) + 1):
            print(str.count(str[:i]))
            # if str.count(str[:1]) > len(mx):
        return mx

if __name__ == "__main__":
    s = input()
    x = repeatedSubstringPattern(s)
    if x:
        print(x)
    else:
        print(-1)
    