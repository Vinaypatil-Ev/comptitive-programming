import LinkedList

class ll(LinkedList.LL):    
    def reverse_group_wrap(self, head, k):
        if head is None:
            return
        count = 0
        temp = head
        while temp and count < k:
            temp = temp.next
            count += 1
        if count != k:
            return head
        x = self.reverse_group_wrap(temp, k)
        curr = head
        pre = None
        while curr != temp :
            next_ = curr.next
            curr.next = pre
            pre = curr
            curr = next_
        head.next = x
        return pre    
        


    
    def reverse_in_group(self, k):
        self.head = self.reverse_group_wrap(self.head, k)


if __name__ == "__main__":
    l = ll()
    x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in x:
        l.add(i)
    l.printList()
    l.reverse_in_group(3)
    l.printList()

