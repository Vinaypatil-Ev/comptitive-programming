def max_sum_sub_seq(arr, n, k):
  s = 0
  for i in range(k):
    s += arr[i]
  w_sum = s
  for i in range(n-k):
    w_sum = w_sum - arr[i] + arr[k+i]
    if w_sum > s:
      s = w_sum
  return s
arr = [100, 200, 300, 400]
s = max_sum_sub_seq(arr, len(arr), 2)
print("max sum", s)     



