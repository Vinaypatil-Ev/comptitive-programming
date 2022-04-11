def lswp(s: str) -> int:
    n = len(s)
    l = r = 0
    vis = set()
    max_len = 0
    ans = ""
    while r < n:
        while s[r] in vis:
            vis.remove(s[l])
            l += 1
        vis.add(s[r])
        r += 1
        if max_len < r - l:
            max_len = r - l
            ans = s[l:r]
    return ans

if __name__ == "__main__":
    print(lswp(input()))