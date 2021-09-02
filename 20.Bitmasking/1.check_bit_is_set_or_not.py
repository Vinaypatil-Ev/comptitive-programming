# check whether kth bit is set or not

def is_set(no, k):
    return no & (1 << (k - 1))

def count_ones(no):
    count = 0
    for i in range(1, len(str(no)) + 1):
        print(is_set(no, i))
        if is_set(no, i):
            count += 1
    return count

if __name__ == "__main__":
    no = 21
    k = 2
    if is_set(no, k):
        print(f"bit at {k} loc is 1")
    else:
        print("not")
    
    print(f"no of ones in no {no}")
    print(count_ones(no))