from removeDuplicates import Solution, LinkNode

def main():
    list1 = LinkNode(1, LinkNode(1, LinkNode(4)))
    #list2 = ListNode(2, ListNode(3, ListNode(4)))
    tester = Solution()
    print(tester.deleteDuplicates(list1))

if __name__ == "__main__":
    main()
