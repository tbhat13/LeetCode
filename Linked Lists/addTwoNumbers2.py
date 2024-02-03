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


        