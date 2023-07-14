#Leetcode https://leetcode.com/problems/climbing-stairs/


# Big O 
# Time - O(n)
# Space - O(n)
class Solution:

    def climbStairs(self, n):
        
        steps = [0] * (n + 1)

        if n == 0:
            return 0

        if n == 1:
            return 1


        steps[0] = 1
        steps[1] = 2

        for i in range(2, n + 1):
            steps[i] = steps[i - 1] + steps[i - 2]

        return steps[n - 1]
        
solution = Solution()
print(solution.climbStairs(45))