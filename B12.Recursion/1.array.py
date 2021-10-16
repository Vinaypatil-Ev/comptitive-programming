def print_f(arr, n):
    if n >= 0:
        print(arr[n], end=" ")
        print_f(arr, n - 1)

def print_r(arr, n):
    if n >= 0:
        print_r(arr, n - 1)
        print(arr[n], end=" ")


if __name__ == "__main__":
    arr = [100, 200, 300, 400, 500, 600, 700, 800, 900]
    print_f(arr, len(arr) - 1)
    print()    
    print_r(arr, len(arr) - 1)
