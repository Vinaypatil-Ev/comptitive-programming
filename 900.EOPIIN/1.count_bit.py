def count_bit(x):
    """
    count no of set bits
    """
    
    count = 0
    while x:
        count += x & 1
        x >>= 1
    return count


if __name__ == "__main__":
    x = 12
    print(count_bit(x), f"no bits in {x}")