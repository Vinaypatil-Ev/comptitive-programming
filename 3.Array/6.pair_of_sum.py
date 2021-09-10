# brute force solution
def pair_of_sum(arr, n, s):
    for i in range(n):
        for j in range(i+1, n):
            if arr[i] + arr[j] == s:
                print(f"force: {arr[i]}, {arr[j]}")
                break

# O(N) O(1)
def pair_of_sum_on(arr, n, s):
    arr.sort() #O(nlogn)
    low = 0
    high = n-1
    while low < high:
        if arr[low] + arr[high] == s:
            print(f"sort: {arr[low]}, {arr[high]}")
            # break
        if arr[low] + arr[high] < s:
            low += 1
        else:
            high -= 1
# O(n)
def pair_of_sum_map(arr, n, s):
    d = {}
    for i in range(n):
        if s - arr[i] in d:
            print(f"map: {s - arr[i]}, {arr[i]}")
        d[arr[i]] = i
    
if __name__ == "__main__":
    arr = [1, 5, 6, 7, 8, 4, 9, 2]
    pair_of_sum(arr, len(arr), 10)
    pair_of_sum_on(arr, len(arr), 10)
    pair_of_sum_map(arr, len(arr), 10)