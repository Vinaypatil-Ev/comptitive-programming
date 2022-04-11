def deleteOdd(listHead):
    l = listHead
    def deleteNode(key, l):
        temp = l
        if(temp != None and temp.data == key):
            return temp.next
            # return
        while(temp != None and temp.data != key):
            prev = temp
            temp = temp.next
        if(temp == None):
            return l
        prev.next = temp.next
        return l
        
    ptr = l
    while(ptr != None):
        if(ptr.data % 2 != 0):
            l = deleteNode(ptr.data, l)
        ptr = ptr.next
    return l












class Node:
    def __init__(self, data):
        self.next = None
        self.data = data
def pri(head):
    temp = head
    while temp:
        print(temp.data, end="-")
        temp = temp.next
    print()
    
l = Node(5)
l.next = Node(2)
l.next.next = Node(3)
l.next.next.next = Node(4)
l.next.next.next.next = Node(6)

pri(l)
l = deleteOdd(l)
pri(l)
    