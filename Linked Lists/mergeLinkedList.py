class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

    def __str__(self, ll):
        result = []
        current = ll
        while current:
            result.append(current.value)  
            current = current.next

        return result

class Solution:
    def main(self,list1, list2):
        merged = output = ListNode()
        while list1 and list2:
            if list1.value < list2.value:
                output.next = list1
                list1 = list1.next
            else:
                output.next = list2
                list2 = list2.next
            output = output.next
        
        if list1:
            output.next = list1
        else:
            output.next = list2

        return ListNode().__str__(merged.next)
            






    if __name__ == "__main__":
        main()