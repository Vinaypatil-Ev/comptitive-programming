import math
def pps(n):
    no = 0
    temp = n
    while temp != 0:
        no = no * 10 + temp % 10
        temp //= 10
    sq = int(math.sqrt(n))
    if no == n:
        if sq * sq == n:
            return 1
        return 0
    else:
        return 0



if __name__ == "__main__":
    # arr = [121, 11, 22, 353, 676, 909]
    arr = list(map(int, input().split()))
    for i in arr:
        print(pps(i), end=" ")
    # print([i*i for i in range(50)])