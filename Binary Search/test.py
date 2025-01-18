from sqrtX import Solution

def test_solution():

    sol = Solution()
    # Test cases for searchInsert
    assert sol.mySqrt(5) == 2  # Answer rounded DOWN to 2 for 2.2
    assert sol.mySqrt(23) == 2  # Answer rounded DOWN to 4 for 4.8
    assert sol.mySqrt(16) == 4  # Answer is an interger
    assert sol.mySqrt(0) == 0  # Answer is 0


