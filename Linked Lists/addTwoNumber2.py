from llist import sllist

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class OtherSolution(object):
    def addTwoNumbers2(self, l1, l2):
        list1 = sllist(l1)
        print(list1)