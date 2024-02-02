class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def append(self, val):
        new_node = ListNode(val)
        current = self
        while current.next:
            current = current.next
        
            current.next = new_node


class Solution(object):
    def removeElements(self, head, val):
        new_list = ListNode()
        current = head
        
        while current:
            if current.val != val:
                new_list.append(current)
        return new_list