class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self, ll):
        result = []
        current = ll
        while current:
            result.append(current.val)  
            current = current.next

        return result


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        head = current = None
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1 + val2 + carry
            carry, digit = divmod(total, 10)

            if current is None:
                head = current = ListNode(digit)
            else:
                current.next = ListNode(digit)
                current = current.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return ListNode().__str__(head)
    
