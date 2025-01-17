from searchInsertPosition import Solution

def test_solution():
    nums = [1, 3, 5, 6]
    sol = Solution()
    # Test cases for searchInsert
    assert sol.searchInsert(nums, 5) == 2  # Target found at index 2
    assert sol.searchInsert(nums, 2) == 1  # Target should be inserted at index 1
    assert sol.searchInsert(nums, 7) == 4  # Target should be inserted at index 4
    assert sol.searchInsert(nums, 0) == 0  # Target should be inserted at index 0
    assert sol.searchInsert([1], 0) == 0  # Single-element list, target inserted at 0
    assert sol.searchInsert([1, 3], 2) == 1  # Two-element list, target inserted in the middle
    assert sol.searchInsert([1, 3], 0) == 0  # Two-element list, target inserted in the beggining

