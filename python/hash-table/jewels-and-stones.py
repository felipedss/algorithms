# https://leetcode.com/problems/jewels-and-stones/


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:

        dict = {}
        for str in jewels:
            dict[str] = 1

        counter = 0
        for str in stones:
            if dict.get(str):
                counter += 1

        return counter


solution = Solution()
print(solution.numJewelsInStones("aA", "aAAbbbb"))
print(solution.numJewelsInStones("z", "ZZZ"))
