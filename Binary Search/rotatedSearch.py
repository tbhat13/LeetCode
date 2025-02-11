class Solution(object):
    def NormalSearch(self, nums, target):
        nums.sort()
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                high = mid -1 
            else:
                low = mid + 1
        return -1
    def search(self, nums, target):
        pivotIdx = 0
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] >= 
            




def main():
    sol = Solution()
    nums = [4,5,6,7,0,1,2]
    print(sol.search(nums, 2))


main()