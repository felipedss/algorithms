# https://leetcode.com/problems/plus-one/


class Solution:
    def plus_one(self, digits):

        for pos, digit in enumerate(digits):
            
            dec_pos = len(digits) - pos - 1

            if digits[dec_pos] == 9:
                digits[dec_pos] = 0
            else:
                digits[dec_pos] = digits[dec_pos] + 1 
                break
            
        if digits[0] == 0:
            digits = [1] + digits

        return digits



solution = Solution()
solution.plus_one([1, 2, 3])
solution.plus_one([4, 3, 2, 1])
solution.plus_one([9])
solution.plus_one([9,9,9,9,9])
solution.plus_one([8,9,9,9])


