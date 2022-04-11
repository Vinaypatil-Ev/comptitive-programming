
class Node:
    def __init__(self, x, pre_ = None, next_ = None):
        self.val = x
        self.pre = pre_
        self.next = next_


class stack:
    def __init__(self):
        self.head = None
        self.count = 0
        self.top = None
        self.mid = None

    def push(self, x):
        self.count += 1
        new_node = Node(x)
        if not self.head:
            self.head = new_node
            self.top = new_node
            self.mid = new_node
            return  
        self.top.next = new_node
        new_node.pre = self.top
        self.top = new_node
        if self.count % 2 == 0:
            self.mid = self.mid.next
        

    def pop(self):
        if self.top:
            self.count -= 1
            print("Item popped is %d" % (self.top.val))
            self.top = self.top.pre
            if self.count % 2:
                self.mid = self.mid.pre
            if self.top: self.top.next = None
            

    def findMiddle(self,):
        return self.mid.val
        

    def deleteMiddle(self):
        if not self.mid.next:
            self.mid = None
        if self.mid:
            self.count -= 1
            print("Deleted Middle Element is %d" % self.mid.val)
            mid = self.mid.next if self.count == 0 else self.mid.pre
            self.mid.pre.next = self.mid.next
            self.mid.next.pre = self.mid.pre
            self.mid = mid

if __name__ == "__main__":
    st = stack()
    st.push(11) 
    st.push(22)
    st.push(33)
    st.push(44)
    st.push(55)
    st.push(66)
    st.push(77)
    st.pop()
    st.pop()
    st.pop()
    print("Middle Element is %d" % st.findMiddle())
    st.deleteMiddle()
    print("Middle Element is %d" % st.findMiddle())

