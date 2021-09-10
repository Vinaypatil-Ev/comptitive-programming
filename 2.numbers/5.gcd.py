def gcd(a, b):
    if a == 0:
        return b
    if b == 0:
        return a
    if a == b:
        return a
    if a > b:
        return gcd(a-b, b)
    return gcd(a, b-a)

def gcd2(a, b):
    if b == 0:
        return a
    return gcd2(b, a%b)
print(gcd(12, 8))
print(gcd2(12, 8))