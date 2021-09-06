def is_prime(no):
    if no < 1:
        return False
    if no == 3 or no == 2:
        return True
    for i in range(2, no//2 + 1):
        if no % i == 0:
            return False
    return True
       
def check(arr):
    left = 0
    right = 0
    for i in range(len(arr)):
        if is_prime(arr[i]):
            arr[left], arr[i] = arr[i], arr[left]
            left += 1
            right += 1
        else:
            arr[right], arr[i] = arr[i], arr[right]
            right += 1
    return arr

if __name__ == "__main__":
    size = int(input())
    arr = list(map(int, input().strip().split()))
    x = check(arr)
    for i in x:
        print(i, end=" ")