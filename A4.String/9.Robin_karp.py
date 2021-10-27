p = 31
m = 1e9 + 9
a = ord("A")

def long_hash(s, start, n):

    curr_hash = 0
    pw = 0
    for i in range(n-1, start-1, -1):
        curr_hash = (curr_hash + ((ord(s[i]) - a + 1) * ((p ** (pw)))))
        pw += 1
    return curr_hash

def all_hash(s):
    t = 0
    d = {}
    for i in range(10, len(s)+1):
        x = long_hash(s, i-10, i)
        d[x] = d.get(x, 0) + 1
        # print(x, t, s[i-10:i])
        t += 1
    print(d)

def rabin_karp(s):
    pass
if __name__ == "__main__":
    s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
    x = long_hash(s, 0, 10)
    y = (ord(s[0]) - a + 1) * ((p ** (9)))
    w = (ord(s[10]) - a + 1) * ((p ** (0)))
    z = (((x - y) * p)+ w)
    all_hash(s)
    print(x, y, w, z)


    
