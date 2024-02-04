from llist import sllist

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def display(self, ll):
        result = []
        current = ll
        while current:
            result.append(current.val)
            current = current.next
        return result

class Solution(object):
    def removeNthFromEnd(self, head, n):
        new_ll = ListNode(0)
        new_ll.next = head
        fast = slow = new_ll

        for _ in range(n):
            fast = fast.next
        
        while fast.next:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next
    
        return ListNode().display(new_ll.next)
    
class OtherSolution(object):
    def removeNthFromEnd(self, head, n):
        lst = sllist(ListNode().display(head))
        node_to_remove = lst.nodeat(-n)
        lst.remove(node_to_remove)
        return lst


