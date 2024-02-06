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
    def deleteDuplicates(self, head):
        dummy = ListNode()
        dummy.next = head
        slow, fast = dummy, head

        while fast:
            if fast.next and fast.val == fast.next.val:
                while fast.next and fast.val == fast.next.val:
                    fast = fast.next
                slow.next = fast.next
            else:
                slow = slow.next
            fast = fast.next

        return ListNode().display(dummy.next)

 
             
            
            
            
        
                

        


        return None

        
