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
    def reverseBetween(self, head, left, right):
        if not head or not head.next or left == right:
            return head
        dummy = ListNode()
        dummy.next = head
        before = dummy
        for i in range(left - 1):
            before = before.next
        new_list, current = None, before.next
        for i in range(right - left + 1):
            next_node = current.next
            current.next = new_list
            new_list = current
            current = next_node
        
        before.next.next = current
        before.next = new_list
        return dummy.next


