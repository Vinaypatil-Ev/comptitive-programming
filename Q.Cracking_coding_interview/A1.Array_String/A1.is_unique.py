# def is_unique(s):
#     d = set()
#     for i in s:
#         if i not in d:
#             d.add(i)
#         elif i in d:
#             return False
#     return True

def is_unique(s):
    bit_arr = 0
    a = ord("a")
    for i in s:
        ith = ord(i) - a
        if bit_arr & (1 << ith):
            return False
        bit_arr |= (1 << ith)
    return True
    


if __name__ == "__main__":
    s = input().strip()
    x = is_unique(s)
    print(x)