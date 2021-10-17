# Insertion sort on Linked list


## Algorithm

1. create the dummy node with value INT_MIN (python float("-inf")) and make its next to head of linked list
2. Scan the LL from left to right. Extract(remove) the node which is samller than its previous node by making previous's next pointer point to the next of that node. Store that node in curr variable
3. Again scan the LL from left to right. Compare the value of extracted node to each node in the list untill you get value greater than the value of extracted node
4. Return next of dummy node

## Code - python

```py
def insertion_sort(head)
        if not head or not head.next:
            return head
  
        dummy = ListNode(float("-inf"))
        dummy.next = head
        temp = head.next
        pre = head
        while temp:
            Next = temp.next
            if pre.val > temp.val:
                curr = temp
                curr.next = None
                pre.next = Next
                pre2 = dummy
                temp2 = dummy.next
                while temp2 and curr.val > temp2.val:
                    pre2 = temp2
                    temp2 = temp2.next
                pre2.next = curr
                curr.next = temp2
            else:
                pre = temp
            temp = Next
  
        return dummy.next
```

###### Time complexity - O(n^2)

###### Space Complexity - O(1)
