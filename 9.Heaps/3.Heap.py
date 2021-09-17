class Heap:
    def __init__(self, cap):
        self.cap = cap
        self.size = 0
        self.heap = []
    
    def max_heapify(self, i):
        left = 2 * i + 1
        right = 2 * i + 2
        largest = None
        if left < self.size and self.heap[left] > self.heap[i]:
            largest = left
        else:
            largest = i
        if right < self.size and self.heap[right] > self.heap[largest]:
            largest = right
        if largest != i:
            self._swap(i, largest)
            self.max_heapify(largest)
    
    def min_heapify(self):
        pass
    
    def extract_max(self):
        if self.size < 1:
            raise OverflowError("heap underflow")
        if self.size == 1:
            self.size = 0
            return self.heap.pop()
        ele = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.size -= 1
        self.max_heapify(0)
        return ele
    
    def extract_min(self):
        pass
    
    def increase_key(self):
        pass
    
    def decrease_key(self):
        pass
    def _swap(self, x, y):
        self.heap[x], self.heap[y] = self.heap[y], self.heap[x]
    def insert_key(self, key):
        if self.size == self.cap:
            print(f"insertion failed heap overflow {key}")
            return
        self.size += 1
        i = self.size - 1
        self.heap.append(key)
        while i > 0 and self.heap[(i - 1) // 2] < self.heap[i]:
            self._swap((i - 1) // 2, i)
            i = (i - 1) // 2


if __name__ == "__main__":
    arr = [3, 6, 45, 23, 7, 9, 100, 54, 89]
    h = Heap(100)
    for i in arr:
        h.insert_key(i)
    print(h.heap)
    print(h.extract_max())
    print(h.extract_max())
    
