class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



class Solution(object):
    def removeElements(self, head, val):
        new_list = ListNode()
        new_list.next = head
        current = new_list
        
        while current:
            if current.val != val:
                new_list.next.val = current.val
            else:
                current = current.next
        return new_list.next