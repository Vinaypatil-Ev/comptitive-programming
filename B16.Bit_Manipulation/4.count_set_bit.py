def count_set_bit(x):
    """
    O(N) time complexity
    O(1) space complexity
    """
    count = 0
    while x:
        count += x & 1
        x >>= 1
    return count

def count_set_bit_pos(x):
    """
    O(N) time complexity
    O(1) space complexity
    """
    count = 0
    pos = 1
    arr = []
    while x:
        if x & 1:
            count += 1
            arr.append(pos)
        x >>= 1
        pos += 1
    return count, arr



if __name__ == "__main__":
    x = 12
    print(count_set_bit(x))
    print(count_set_bit_pos(x))