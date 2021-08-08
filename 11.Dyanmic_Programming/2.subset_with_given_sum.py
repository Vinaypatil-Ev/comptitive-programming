def subset_sum(arr, s, n):
    if s == 0:
        return True
    if n == 0 and s != 0:
        return False
    if arr[n - 1] > s:
        subset_sum(arr, s, n - 1)
    return subset_sum(arr, s, n - 1) or subset_sum(arr, s - arr[n - 1], n - 1) 

if __name__ == "__main__":
    arr = [1, 2, 3]
    s = 0
    n = len(arr)
    x = subset_sum(arr, s, n)
    if x:
        print("sum is possible")
    else:
        print("not possible")
        
"""
[1, 2, 3]
s = 5
1 2 1
2 3 3
"""