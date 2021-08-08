# find largest sum cuntinous subarray
def max_sum_subarr(arr):
    s = float("-inf")
    c = 0
    for i in arr:
        c = max(0, c + i)
        s = max(s, c)
    return s
# problem in the above solution is 
# it will return maximus sum as 0 
# if all the elemnt in the array are negative

# optimised solution
def max_sum_subarr2(arr):
    s = float("-inf")
    c = 0
    for i in arr:
        c = c + i
        if c > s:
            s = c
        if c < 0:
            c = 0
    return s

if __name__ == "__main__":
    # arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    arr = [-2, -1, -3, -4, -1, -2, -1, -5, -4, -100]
    x = max_sum_subarr(arr)
    x2 = max_sum_subarr2(arr)
    print(x)
    print(x2)