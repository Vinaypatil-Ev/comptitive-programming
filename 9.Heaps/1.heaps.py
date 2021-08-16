class Heap:
    def __init__(self):
        self.heap = None
    def create_heap(self, arr):
        n = len(arr)
        self.heap = arr.copy()
        # for i in arr:
        #     self.heap.append(i)
        for i in range(max(0, n // 2 - 1), -1, -1):
            self.__sink(i)
    def size(self):
        return len(self.heap)
    def __less(self, x, y):
        return self.heap[x] < self.heap[y]
    def __swap(self, x, y):
        self.heap[x], self.heap[y] = self.heap[y], self.heap[x]
    def __sink(self, i):
        heap_size = self.size()
        while True:
            left = 2 * i + 1
            right = 2 * i + 2
            smaller = left
            if right < heap_size and self.__less(right, left):
                smaller = right
            if left > heap_size or self.__less(i, smaller):
                break
            self.__swap(i, smaller)
            i = smaller
    def __str__(self):
        return str(self.heap)
            
        
if __name__ == "__main__":
    heap = Heap()
    arr = [1, 2, 2, 5, 6, 7, 8, 9, 2, 3, 4, 0, 1, 2, 1] 
    heap.create_heap(arr)
    print(heap)
    
    