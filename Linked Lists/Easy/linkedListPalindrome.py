class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def isPalindrome(self, head):
        slow = fast = head
        while fast.next:
            slow = slow.next
            fast = fast.next.next

        part1, part2 = [], []
        fast, slow = slow, head
        while fast:
            part1.append(fast.val)
            part2.append(slow.val)
            fast, slow = fast.next, slow.next
        part2.reverse()
        return part1 == part2