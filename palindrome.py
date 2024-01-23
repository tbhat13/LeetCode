class Solution():
    def isPalindrome(self, x):
        if not(-2**31 <= x <= 2**31 - 1):
            return "Invalid value: x is not in range"
        if str(x)[::-1] == str(x):
            return True
        return False