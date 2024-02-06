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
        current = length_finder = head
        length = 0
        while length_finder:
            length_finder = length_finder.next
            length+= 1
        if k % length == 0: return head
        for _ in range(k%length):
            while current.next.next:
                current = current.next
            new_head = current.next
            current.next = None
            new_head.next = head
            current = head = new_head
        
        return new_head
    
class OtherSolution(object):
    def rotateRight(self, head, k):
        list1 = sllist(ListNode().display(head))
        list1.rotate(k)
        return list1
    
