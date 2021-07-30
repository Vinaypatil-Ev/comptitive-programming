def diff_update_sum(arr, d):
    for i in range(len(arr)):
        if i == 0:
            arr[i] = d[i]
        else:
            arr[i] = d[i] + arr[i-1]
        
def add_and_sub_update(arr, x, y, value):
    arr[x] += value
    arr[y+1] -= value

def create_diff_arr(arr, n):
    d = [0] * (n + 1)
    d[0] = arr[0]
    for i in range(1, n):
        d[i] = arr[i] - arr[i-1]
    return d


if __name__ == "__main__":
    arr = [10, 5, 20, 40]
    print("array:", arr)
    diff = create_diff_arr(arr, len(arr))
    add_and_sub_update(diff, 0, 1, 10)
    add_and_sub_update(diff, 1, 3, 20)
    add_and_sub_update(diff, 2, 2, 20)
    diff_update_sum(arr, diff)
    print(arr)












