from linkedListIntersection import Solution, ListNode

def main():
    list1 = ListNode(1, ListNode(1, ListNode(4)))
    list2 = ListNode(2, ListNode(3, ListNode(4)))
    tester = Solution()
    print(tester.getIntersectionNode(list1, list2))

if __name__ == "__main__":
    main()
