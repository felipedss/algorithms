# Leetcode - https://leetcode.com/problems/find-the-town-judge/

from collections import defaultdict

class Solution:

    def findJudge(self, N, trust):
        trust_bucket = [0] * (N + 1)  # Contagem de confiança

        for a, b in trust:
            trust_bucket[a] -= 1  # como a pessoa confia em alguem, decrementa-se o contador de confiança dela
            trust_bucket[b] += 1  # como a pessoa b é confiável, incrementa-se o contador de confiança dela

        for i in range(1, N + 1):
            if trust_bucket[i] == N - 1:
                return i

        return -1

solution = Solution()
print(solution.findJudge(2, [[1,2]]))