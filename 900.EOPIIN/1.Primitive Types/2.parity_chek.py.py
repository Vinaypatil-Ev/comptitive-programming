def check_pariy(x):
    """
    TC: O(n): n = size of word
    
    """
    _is = 0
    while x:
        _is ^= x & 1
        x >>= 1
    return _is

def parity_check2(x):
    """
    
    """
    _is = 0
    while x:
        _is ^= 1
        x &= x - 1
    return _is



if __name__ == "__main__":
    x = 11
    # print(check_pariy(x))
    print(parity_check2(x))