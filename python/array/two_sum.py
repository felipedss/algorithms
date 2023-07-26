# Leetcode https://leetcode.com/problems/two-sum/

class Solution:

    def two_sum(self, nums, target):

        num_post_dic = {}

        for i, num in enumerate(nums):

            complement = target - num

            # Check if complement is present on dict
            if complement in num_post_dic:
                return num_post_dic[complement], i

            num_post_dic[num] = i

        return []


solution = Solution()
print(solution.two_sum([2,7,11,15], 9))
print(solution.two_sum([3, 2, 4], 6))
print(solution.two_sum([3, 3], 6))
