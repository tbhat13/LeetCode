from rotateList import OtherSolution, ListNode



def main():
    list1 = ListNode(1)
    list1.next = ListNode(2)
    list1.next.next = ListNode(3)
    list1.next.next.next = ListNode(4)
    list1.next.next.next.next = ListNode(5)
    n = 2
    list2 = ListNode(1)

    tester = OtherSolution()
    print(tester.rotateRight(list1, n))



if __name__ == "__main__":
    main()
