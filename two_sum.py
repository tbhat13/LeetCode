class Solution(object):
    def twoSum(self, nums, target):
        #Check if list, nums, has a length between 2 and 10^4
        if not (2 <= len(nums) <= 10**4):
            return "Invalid input: Length of nums should be between 2 and 10^4."
        
        #Check if each element is between -10^9 and 10^9
        for num in nums:
            if not (-10**9 <= num <= 10**9):
                return "Invalid input: Elements in nums should be between -10^9 and 10^9."
            
        #Check if target is between  -10^9 and 10^9
        if not (-10**9 <= target <= 10**9):
            return "Invalid input: Target should be between -10^9 and 10^9."
        
        #Non invalid inputs evaluated
        for index, number in enumerate(nums):
            other_num = target - number
            if other_num in nums[index+1:]:
                return [index, nums.index(other_num, index+1)]