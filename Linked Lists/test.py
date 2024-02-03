from addTwoNumbers2 import ListNode, OtherSolution

def main():
    list1 = ListNode(0)
    list1.next = ListNode(8)
    list1.next.next = ListNode(6)
    list1.next.next.next = ListNode(5)
    list1.next.next.next.next = ListNode(6)
    list1.next.next.next.next.next = ListNode(8)
    list1.next.next.next.next.next.next = ListNode(3)
    list1.next.next.next.next.next.next.next = ListNode(5)
    list1.next.next.next.next.next.next.next.next = ListNode(7)

    list2 = ListNode(6)
    list2.next = ListNode(7)
    list2.next.next = ListNode(8)
    list2.next.next.next = ListNode(0)
    list2.next.next.next.next = ListNode(8)
    list2.next.next.next.next.next = ListNode(5)
    list2.next.next.next.next.next.next = ListNode(8)
    list2.next.next.next.next.next.next.next = ListNode(9)
    list2.next.next.next.next.next.next.next.next = ListNode(7)


    tester = Solution()
    print(tester.addTwoNumbers(list1, list2))
    tester.addTwoNumbers2(list1, list2)

if __name__ == "__main__":
    main()
