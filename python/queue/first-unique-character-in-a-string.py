# https://leetcode.com/problems/first-unique-character-in-a-string/description/

"""
The checked variable optimizes the code, once:
- text[index] not in checked = O(n)
- text.count(text[index]) == 1 = O(nˆ2)

This solution runtime is 5409 ms:
for index in range(0, len(s)):
    if s.count(s[index]) == 1:
        return index
return -1

"""

# O(n)
# the current runtime 74 ms 
class Solution:
    def firstUniqChar(self, text):
        checked = set()
        for index in range(0, len(text)):
            if text[index] not in checked and text.count(text[index]) == 1:
                return index
            else:
                checked.add(text[index])
        return -1


solution = Solution()

assert solution.firstUniqChar("aaa") ==  -1
assert solution.firstUniqChar("leetcode") == 0
assert solution.firstUniqChar("loveleetcode") == 2
assert solution.firstUniqChar("aabb") == -1