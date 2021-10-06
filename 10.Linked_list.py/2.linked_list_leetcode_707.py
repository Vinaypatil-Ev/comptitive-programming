class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
    def is_head(self):
        return self.head != None
    def get_nth_node_and_pre(self, index, tout=False):
        temp = self.head
        pre = temp
        while temp and index:
            pre = temp
            temp = temp.next
            index -= 1
        if index > 0:
            return
        if tout:
            return temp
        return pre
    def get(self, index):
        if not self.is_head():
            return -1
        temp = self.get_nth_node_and_pre(index, True)
        if temp:
            return temp.val
        return -1
    
    
    def add_at_head(self, val):
        if not self.is_head():
            self.head = Node(val)
            return
        node = Node(val)
        node.next = self.head
        self.head = node
        
    def add_at_tail(self, val):
        if not self.is_head():
            self.head = Node(val)
            return
        pre = self.get_nth_node_and_pre(-1)
        node = Node(val)
        pre.next = node
        
    def add_at_index(self, index, val):
        if not self.is_head() and index > 0:
            return
        if index == 0:
            self.add_at_head(val)
            return
        pre = self.get_nth_node_and_pre(index)
        node = Node(val)
        node.next = pre.next
        pre.next = node
        
    def delete_at(self, index):
        if not self.is_head():
            return
        if index == 0:
            self.head = self.head.next
            return
        pre = self.get_nth_node_and_pre(index)
        if pre and pre.next:
            pre.next = pre.next.next
    # def add_at(self, index)
    def __str__(self):
        r = ""
        temp = self.head 
        while temp:
            r = r + str(temp.val) + " "
            temp = temp.next
        return r
            


if __name__ ==  "__main__":
    ll = None
    op = ["MyLinkedList","addAtHead","addAtTail","addAtIndex","get","deleteAtIndex","get","get","deleteAtIndex","deleteAtIndex","get","deleteAtIndex","get"]
    s = [[],[1],[3],[1,2],[1],[1],[1],[3],[3],[0],[0],[0],[0]]
    l = []
    x = ""
    for i in range(len(op)):
        if op[i] == "MyLinkedList":
            ll = LinkedList()
        elif op[i] == "addAtHead":
            x = ll.add_at_head(s[i][0])
        elif op[i] == "addAtIndex":
            x = ll.add_at_index(s[i][0], s[i][1])
        elif op[i] == "deleteAtIndex":
            x = ll.delete_at(s[i][0])
        elif op[i] == "addAtTail":
            x = ll.add_at_tail(s[i][0])
        elif op[i] == "get":
            x = ll.get(s[i][0])
        print("---", ll)
        print(x)
        l.append(x)
    print(l)