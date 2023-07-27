# LeetCode https://leetcode.com/problems/roman-to-integer/


class Solution:
    def romanToInt(self, s) -> int:

        dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        sum = 0
        for pos in range(len(s)):

            key = s[pos]
            value = dict.get(key)

            if pos == len(s) - 1:
                sum = sum + value
            else:
                next_key = s[pos + 1]
                value_next = dict.get(next_key)
                sum = sum + value if value >= value_next else sum - value

        return sum


solution = Solution()
print(solution.romanToInt("MCMXCIV"))
print(solution.romanToInt("MMMDC"))
print(solution.romanToInt("LVIII"))
print(solution.romanToInt("III"))
print(solution.romanToInt("II"))
print(solution.romanToInt("I"))
print(solution.romanToInt("MM"))
print(solution.romanToInt("MML"))
print(solution.romanToInt("MLM"))
