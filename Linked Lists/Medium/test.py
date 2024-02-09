from reverseLinkedList2 import Solution, ListNode



def main():
    list1 = ListNode(1)
    list1.next = ListNode(1)
    list1.next.next = ListNode(2)
    list1.next.next.next = ListNode(3)
    list1.next.next.next.next = ListNode(3)
    list1.next.next.next.next.next = ListNode(4)
    list1.next.next.next.next.next.next = ListNode(4)
    list1.next.next.next.next.next.next.next = ListNode(5)
    left = 2
    right = 4
    list2 = ListNode(1)
    list2.next = ListNode(2)
    list2.next.next = ListNode(3)
    list2.next.next.next = ListNode(4)
    list2.next.next.next.next = ListNode(5)
    #list2.next.next.next.next.next = ListNode(6)
    #list2.next.next.next.next.next.next = ListNode(7)

    tester = Solution()
    print(tester.reverseBetween(list2, left, right))



if __name__ == "__main__":
    main()
