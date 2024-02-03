from llist import sllist

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
        
class OtherSolution(object):
    def middleNode(self, head):
        linked_list_values = []
        while head:
            linked_list_values.append(head.val)
            head = head.next

        list1 = sllist(linked_list_values)
        midpoint = list1.size
        return list1.nodeat(midpoint//2).value

