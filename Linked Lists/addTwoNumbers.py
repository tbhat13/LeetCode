from llist import sllist

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def ll_to_list(self, ll):
        list = []
        current = ll
        while current:
            list.append(current.val)
            current = current.next
        return list


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
    
class OtherSolution(object):
    def addTwoNumbers(self, l1, l2):
        list1 = sllist(ListNode().ll_to_list(l1))
        list2 = sllist(ListNode().ll_to_list(l2))
        result = []
        carry = 0
        for value1, value2 in zip(list1, list2):
            added = value1 + value2 + carry
            if added >= 10:
                carry = 1
            else:
                carry = 0
            result.append(added % 10)

        return sllist(result)
    
