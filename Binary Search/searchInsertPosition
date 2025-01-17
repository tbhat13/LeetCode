class Solution(object):
    def decision_maker(self, nums, target, mid):
        if nums[mid] == target:
            if mid - 1 > 0 and nums[mid - 1] == target:
                return 'right'
            else:
                return 'found'
            
        elif nums[mid] < target:
            return 'right'
        else:
            return 'left'


    def searchInsert(self, nums, target):
        low, high = 0, len(nums) - 1
        pot_index = 0
        while low <= high:
            mid = int((low + high) / 2)
            result = self.decision_maker(nums, target, mid)
            if result == 'found':
                return mid
            elif result == 'right':
                low = mid + 1
                pot_index = low
            elif result == 'left':
                high = mid - 1
                pot_index = high
        
        return pot_index
        
                

