class LinkNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

    def __str__(self, linkedList):
        result = []
        current = linkedList
        while current:
            result.append(current.value)
            current = current.next

        return result
        

class Solution:
    def deleteDuplicates(self, link1):
        current = link1
        while current and current.next:
            if current.value == current.next.value:
                current.next = current.next.next
            else:
                current = current.next
        
        return LinkNode().__str__(link1)