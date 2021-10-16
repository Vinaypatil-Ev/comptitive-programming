# def even_odd(arr):
#     even = odd = i = 0
#     while i < len(arr):
#         if arr[i] % 2 == 0:
#             even += 1
#             odd += 1
#         else:
#             arr[odd], arr[i] = arr[i], arr[odd]
#             odd += 1
#         i += 1
        
import builtins


def even_odd(arr):
    left = 0
    right = len(arr) - 1
    while left < right:
        if arr[left] % 2 == 0:
            left += 1
        else:
            arr[left], arr[right] = arr[right], arr[left]
            right -= 1


if __name__ == "__main__":
    arr = [9, 1, 2, 5, 4, 8, 11, 10]
    # arr = list(map(int, input().split()))
    # arr = [0, 1, 0, 1, 0, 1]
    even_odd(arr)
    print(arr)
