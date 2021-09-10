from collections import defaultdict as ddict
def wbi(s, wd):
    if len(s) == 0:
        return True
    for i in range(1, len(s)+1):
        if wbi(s[i: ], wd) and s[: i] in wd:  
            return True
    return False


def wbr(s, wd, n, d):
        print(n, dict(d))
        print(n, "in", n not in d)
        if n not in d:
            print("-")
            for i in range(n+1, len(s)+1):
                print(i, "---", len(s))
                if wbr(s, wd, i, d) and s[: i] in wd:
                    d[i] = True
        return d[n]
        
        
if __name__ == "__main__":
    s = input()
    word_dict = set(input().split())
    # x = wbi(s, word_dict)
    # print(x)
    d = ddict(lambda: False)
    d[len(s)] = True
    x = wbr(s, word_dict, 0, d)
    print(x)