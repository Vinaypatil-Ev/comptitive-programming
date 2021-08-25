class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
class LL:
    def __init__(self):
        self.head = None
        
    def add(self, value):
        if self.head is None:
            self.head = Node(value)
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            temp.next = Node(value)
    def printList(self):
        if self.head is None:
            print("list is empty")
        else:
            temp = self.head
            while temp != None:
                print(f"{temp.value} -> ", end="")
                temp = temp.next
            print("Null \n")
    def reverse(self):
        if self.head is None:
            return
        temp = self.head
        pre = None
        while temp != None:
            curr = temp
            temp = temp.next
            curr.next = pre
            pre = curr
        self.head = pre
    def reverse_wrap(self, curr, pre):
        if curr.next is None:
            self.head = curr
            curr.next = pre
            return
        next = curr.next
        curr.next = pre
        self.reverse_wrap(next, curr)
    def reverse_r(self):
        if self.head is None:
            return
        self.reverse_wrap(self.head, None)
    def revg_wrap(self, head, size):
        temp = head
        pre = None
        # next = None
        count = 0
        while temp != None and count < size:
            curr = temp
            temp = temp.next
            curr.next = pre
            pre = curr
            count += 1
        if temp is not None:
            head.next = self.revg_wrap(temp, size)
        return pre
              
            
    def reverse_group(self, size):
        self.head = self.revg_wrap(self.head, size)
        
            
        


if __name__ == "__main__":
    l = LL()
    l.add(32)
    l.add(43)
    l.add(3)
    l.add(99)
    l.add(0)
    l.add(7)
    l.printList()
    # l.reverse()
    # l.printList()
    # l.reverse_r()
    # l.printList()
    l.reverse_group(3)
    l.printList()
        
            