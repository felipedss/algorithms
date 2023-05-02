# https://leetcode.com/problems/add-digits/


# In this implementation, we first check if the number is zero. 
# If it is zero, its sum of digits is zero. 
# Then we check if the number is divisible by 9. If so, its sum of digits is 9. 
# If not, we use the mathematical formula to calculate the sum of digits.

# O (1)
class Solution(object):
    def addDigits(self, num):
        if num == 0:
            return 0
        elif num % 9 == 0:
            return 9
        else:
            return num % 9

solution = Solution()
print(solution.addDigits(438))        