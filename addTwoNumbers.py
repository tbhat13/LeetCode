from llist import sllist

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        num1 = num2 = 0
        solution = 0
        current_l1, current_l2 = l1, l2
        while current_l1:
            num1 = num1 * 10 + current_l1
            current_l1 = current_l1.next
        while current_l2:
            num2 = num2 * 10 + current_l2
            current_l2 = current_l2.next
        solution = num1 + num2
    
        