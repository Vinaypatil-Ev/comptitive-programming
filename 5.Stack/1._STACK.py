class stack:
    def __init__(self, size):
        self.size = size
        self.stack = [None] * size
        self.top = -1
        
    def is_empty(self):
        return self.top == -1
    def is_full(self):
        return self.top == self.size - 1
    def push(self, ele):
        if not self.is_full():
            self.top += 1
            self.stack[self.top] = ele
        else:
            raise Exception(f"Stack is full, push failed {ele}")
    def pop(self):
        if not self.is_empty():
            ele = self.stack[self.top]
            self.stack[self.top] = None
            self.top -= 1
            return ele
        else:
            raise Exception("Stack is empty, Pop failed")
        

if __name__ == "__main__":
    s = stack(6)
    s.push(123)
    s.push(12)
    s.push(23)
    s.push(23)
    s.push(132)
    s.push(143)
    # s.push(343)
    s.pop()
    s.pop()
    s.pop()
    s.pop()
    s.pop()
    s.pop()
    