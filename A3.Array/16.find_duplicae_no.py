def find_duplicate_no(arr):
    slow = 0
    fast = 0
    while True:
        slow = arr[slow]
        fast = arr[arr[fast]]
        if slow == fast:
            break
    slow = 0
    while slow != fast:
        slow = arr[slow]
        fast = arr[fast]
    return slow

def find_duplicate_no2(arr):
    n = len(arr)
    fs = n * (n + 1) / 2
    s = sum(arr)
    print(fs)
    print(s)
    return s - fs


if __name__ == "__main__":
    arr = [4, 3, 7, 8, 6, 9, 2, 1, 5, 2]
    x = find_duplicate_no(arr)
    print(x)
    x = find_duplicate_no2(arr)
    print(x)