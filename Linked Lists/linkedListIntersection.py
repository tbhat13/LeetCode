class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        iter = set()
        current = headA

        while current:
            iter.add(current)
            current = current.next

        current = headB

        while current:
            if current in iter:
                return current
            else:
                iter.add(current)
                current = current.next

        return None
