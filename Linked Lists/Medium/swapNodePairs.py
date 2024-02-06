from llist import sllist

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def display(self, ll):
        list = []
        current = ll
        while current:
            list.append(current.val)
            current = current.next
        return list

class Solution(object):
    def swapPairs(self, head):
        dummy = ListNode(0)
        dummy.next = head
        current = dummy
        while current.next and current.next.next:
            temp = current.next
            current.next = temp.next
            temp.next = temp.next.next
            current.next.next = temp

            current = current.next.next
            

        return ListNode().display(dummy.next)
    
