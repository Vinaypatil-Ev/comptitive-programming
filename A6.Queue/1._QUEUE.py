class queue:
    def __init__(self, cap):
        self.size = 0
        self.cap = cap
        self.q = [None] * cap
        self.front = -1
        self.back = -1
        
    def is_empty(self):
        return self.size == 0
    def is_full(self):
        return self.size == self.cap
    def enqueue(self, ele):
        if not self.is_full():
            self.back = (self.back + 1) % self.cap
            self.q[self.back] = ele
            self.size += 1
        else:
            raise Exception(f"enqueue failed, queue is full {ele}")
    def dequeue(self):
        if not self.is_empty():
            ele = self.q[self.front]
            self.q[self.front] = None
            self.front = (self.front + 1) % self.cap
            self.size -= 1
            return ele
        else:
            raise Exception("dequeue failed, queue is empty")
        

if __name__ == "__main__":
    q = queue(6)
    q.enqueue(122)
    q.enqueue(142)
    q.enqueue(43)
    q.enqueue(132)
    q.enqueue(10)
    q.enqueue(1)
    # q.enqueue(839)
    q.dequeue()
    q.dequeue()
    q.dequeue()
    q.dequeue()
    q.dequeue()
    # q.dequeue()
    q.dequeue()
    q.enqueue(433)
    q.enqueue(433)
    q.enqueue(433)
    q.enqueue(433)
    q.dequeue()
    q.dequeue()
    q.dequeue()
    q.enqueue(433)
    q.enqueue(433)
    q.enqueue(433)
    print(q.q)
    print(q.front)
    print(q.back)
    
    