def main(textInput):
    # textInput = str(input())
    d = {}
    res = []
    for word in textInput.split():
        if word not in d:
            d[word] = 1
        elif word in d:
            if d[word] == 1:
                res.append(word)
            d[word] = d[word] + 1
    res.sort()
    return res

def main(word1, word2):
    if len(word1) != len(word2):
        return -1
    s = word1 + word1
    n = len(word2)
    i = 0
    while i < len(s):
        if s[i] == word2[0]:
            t = i
            k = 0
            while t < len(s) and k < n and s[t] == word2[k]:
                t += 1
                k += 1
            if k == n:
                return 1
        i += 1
    return -1

if __name__ == "__main__":
    # s = "cat batman latt matter cat matter cat"
    # x = main(s)
    x = main("sample", "plesam")
    print(x)