class Solution:
    def searchInsert(self, nums, target):

        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = left + int((right - left) / 2)

            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1

        return left


solution = Solution()
assert solution.searchInsert([1, 2, 3, 4, 5, 7, 8, 9, 10], 6) == 5
assert solution.searchInsert([1, 3, 5, 6], 5) == 2
assert solution.searchInsert([1, 3, 5, 6], 2) == 1
assert solution.searchInsert([1, 3, 5, 6], 7) == 4
