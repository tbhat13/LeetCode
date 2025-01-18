class Solution(object):
    def mySqrt(self, x):
        low,high = 0, x
        while low <= high:
            mid = (low + high) // 2
            if mid * mid < x:
                low = mid + 1
            elif mid * mid > x:
                high = mid - 1
            else:
                return mid

        return high
    
sol = Solution()

# Call the searchInsert method
result = sol.mySqrt(24)
print(result)   
        