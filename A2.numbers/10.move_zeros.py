"""
leetcode - 
https://leetcode.com/problems/move-zeroes/
"""

def move_zeros(arr):
    left = start = 0
    while left < len(arr):
        if arr[left] != 0:
            arr[left], arr[start] = arr[start], arr[left]
            start += 1
        left += 1

if __name__ == "__main__":
    arr = list(map(int, input().split()))
    move_zeros(arr)
    for i in arr:
        print(i, end=" ")