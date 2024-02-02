class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



class Solution(object):
    def removeElements(self, head, val):
        new_list = ListNode()
        new_list.next = head
        current = new_list
        
        while current.next != None:
            if current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next

        return new_list.next
                