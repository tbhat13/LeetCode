class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution(object):
    def middleNode(self, head):
        slow = fast = checker = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        checker = slow
        counter = 0
        while checker:
            checker = checker.next
            counter += 1
        if counter % 2 != 0:
            return slow.val
        else:
            return slow.next.val

