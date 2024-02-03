from addTwoNumbers import Solution, ListNode

def main():
    list1 = ListNode(1)
    list1.next = ListNode(2)
    list1.next.next = ListNode(3)
    list2 = ListNode(4)
    list2.next = ListNode(5)
    list2.next.next = ListNode(6)


    tester = Solution()
    print(tester.addTwoNumbers(list1, list2))

if __name__ == "__main__":
    main()
