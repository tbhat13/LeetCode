from removeLinkedListElems import Solution, ListNode

def main():
    list1 = ListNode(1, ListNode(1, ListNode(4)))
    #list2 = ListNode(2, ListNode(3, ListNode(4)))
    val = 4
    tester = Solution()
    print(tester.removeElements(list1, val))

if __name__ == "__main__":
    main()
