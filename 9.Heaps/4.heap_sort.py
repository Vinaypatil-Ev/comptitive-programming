class Heap:
    def heapify(self, arr, i, size):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        if left < size and arr[left] > arr[largest]:
            largest = left
        if right < size and arr[right] > arr[largest]:
            largest = right
        if largest != i:
            arr[largest], arr[i] = arr[i], arr[largest]
            self.heapify(arr, largest, size)
    def heap_sort(self, arr):
        size = len(arr)
        # heap formation
        for i in range((size) // 2 - 1, -1, -1):
            self.heapify(arr, i, size)
        # heap sort
        for i in range(size - 1, 0, -1):
            arr[0], arr[size - 1] = arr[size - 1], arr[0]
            size -= 1
            self.heapify(arr, 0, size)
            


if __name__ == "__main__":
    arr = list(map(int, input().split()))
    h = Heap()
    h.heap_sort(arr)
    for i in arr:
        print(i, end=" ")
    