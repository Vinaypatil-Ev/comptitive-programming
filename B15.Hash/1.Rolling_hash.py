def hash(s):
    p = 31
    m = 26
    hash_value = 0
    p_pow = 1000
    for c in s:
        hash_value = (hash_value + (ord(c) - ord('a') + 1)**ord(c)) % 1000
    return hash_value

print(hash("duh"))
print(hash("uhd"))
print(hash("hud"))
print(hash("ill"))