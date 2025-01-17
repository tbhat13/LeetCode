class Solution(object):
    def searchInsert(self, nums, target):
        def binary_search(low, high):
            if low > high:
                return low
            
            mid = int((low + high) / 2)
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                return binary_search(mid + 1, high) 
            else:
                return binary_search(low, mid - 1)
        
        return binary_search(0, len(nums) - 1)



# Create an instance of Solution
solution = Solution()

# Call the searchInsert method
result = solution.searchInsert([1, 3], 2)
print(result)
