# https://leetcode.com/problems/number-of-good-pairs/

# Time complexity - O(n^2)

class Solution:
    def numIdenticalPairs(self, nums):
        good_pairs = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j] and i < j:
                    good_pairs += 1

        return good_pairs

    # O(n) solution
    def numIdenticalPairs2(self, nums):
        dict = {}
        res = 0
        for n in nums:            
            if n in dict:
                res += dict[n]
                dict[n] += 1
            else:
                dict[n] = 1
        return res        


solution = Solution()
assert solution.numIdenticalPairs([1, 2, 3, 1, 1, 3]) == 4
assert solution.numIdenticalPairs([1, 1, 1, 1]) == 6
assert solution.numIdenticalPairs([1, 2, 3]) == 0

assert solution.numIdenticalPairs2([1, 2, 3, 1, 1, 3]) == 4
assert solution.numIdenticalPairs2([1, 1, 1, 1]) == 6
assert solution.numIdenticalPairs2([1, 2, 3]) == 0
