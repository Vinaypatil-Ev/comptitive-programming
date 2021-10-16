def cp(word, start, end):
    if start == len(word):
        print("\n---------------------------------------s")
        return
    for i in range(start+1, len(word)+1):
        cp(word, i, end)
        print(" "*(len(word) - len(word[start:i])), word[start:i], end=" ")
        # print()
    print(" "*(len(word) - len(word[start: end])), word[start: end], end=" ")
    print()


if __name__ == "__main__":
    s = "leetcode"
    cp(s, 0, len(s))