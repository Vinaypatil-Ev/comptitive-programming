from collections import defaultdict as ddict
def wbi(s, wd, start):
    if len(s) == 0:
        return True
    for i in range(start + 1, len(s)+1):
        if wbi(s[start:i], wd) and s[: i] in wd:  
            return True
    return False


def wbr(s, wd, start, end, d):
        # if (start, end) not in d:
        #     if s[start: end] in wd:
        #         d[(start, end)] = True
        for i in range(start+1, end+1):
            if (start, i) not in d:
                d[(start, i)] = s[start: i] in wd
            if (i, end) not in d:
                d[(i, end)] = wbr(s, wd, i, end, d)
            if d[(i, end)] and d[(start, i)]:
                d[(start, end)] = True
        return d[(start, end)]
        
        
if __name__ == "__main__":
    s = input()
    word_dict = set(input().split())
    x = wbi(s, word_dict)
    print(x)
    # d = ddict(lambda: False)
    # d[(len(s), len(s))] = True
    # x = wbr(s, word_dict, 0, len(s), d)
    # print(x)