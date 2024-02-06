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
    def rotateRight(self, head, k):
        if k == 0 or head is None or head.next is None: return head
        current = head
        length = 0
        while current.next.next:
            current = current.next
            length+= 1
        length+=2
        if k % length == 0: return head
        for _ in range(k % length):
            new_head = current.next
            current.next = None
            new_head.next = head
            current = head = new_head
            
        return new_head
    

class OtherSolution(object):
    def rotateRight(self, head, k):
        list1 = sllist(ListNode().display(head))
        return list1