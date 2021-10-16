# brute force solution
def max_sub_seq_sum(arr, n, k):
    s = -10000000000000000000
    for i in range(n-k+1):
        t = 0
        for j in range(k):
            t += arr[i+j]
        if s < t:
            s = t
    print(s)

def sliding_window_sum(arr, n, k):
    k_sum = sum(arr[:k])
    w_sum = k_sum
    for i in range(n-k):
        w_sum = w_sum - arr[i] + arr[k+i]
        if w_sum > k_sum:
            k_sum = w_sum
    print(k_sum)

arr = [100, 200, 300, 400]
max_sub_seq_sum(arr, len(arr), 2) 
sliding_window_sum(arr, len(arr), 2)