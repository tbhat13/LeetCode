from addTwoNumbers import OtherSolution, Solution, ListNode



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


    tester1 = Solution()
    tester2 = OtherSolution()
    print(tester1.addTwoNumbers(list1, list2))
    print(tester2.addTwoNumbers(list1, list2))
if __name__ == "__main__":
    main()
