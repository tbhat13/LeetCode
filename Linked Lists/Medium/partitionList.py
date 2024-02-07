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
    def partition(self, head, x):
        start = lesser_than_x = ListNode()
        end = greater_than_x = ListNode()

        while head:
            if head.val < x:
                lesser_than_x.next = head
                lesser_than_x = lesser_than_x.next
            else:
                greater_than_x.next = head
                greater_than_x = greater_than_x.next

            head = head.next

        greater_than_x.next = None
        lesser_than_x.next = end.next
        return start.next



        


        

            
