# Leetcode - https://leetcode.com/problems/remove-element/

class Solution(object):
    def removeElement(self, nums, val):
        counter = 0
        pos = 0
        for num in nums:
            if val != num:
                counter = counter + 1
                nums[pos] = num
                pos = pos + 1

        return counter

solution = Solution()
print(solution.removeElement([1, 2, 3, 4], 2))