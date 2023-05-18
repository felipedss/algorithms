# Leetcode: https://leetcode.com/problems/add-binary/

class Solution:
    def addBinary(self, a, b):
        remaining = 0
        result = ""
        max_length = len(a) if len(a) - len(b) >= 0 else len(b)
        a = a.rjust(max_length, "0")
        b = b.rjust(max_length, "0")

        for pos in range(len(a) - 1, -1, -1):
            sum = int(a[pos]) + int(b[pos]) + remaining
            if sum == 0 or sum == 2:
                remaining = 1 if sum == 2 else remaining
                result = "0" + result
            elif sum == 1 or sum == 3:
                remaining = 0 if sum == 1 else remaining
                result = "1" + result

        result = ("1" if remaining == 1 else "") + result
        return result


solution = Solution()        
assert solution.addBinary("11", "1") == "100"
assert solution.addBinary("1010", "1011") == "10101"
assert solution.addBinary("10101101", "1100110") == "100010011"
assert solution.addBinary("0", "1") == "1"
assert solution.addBinary("0", "0") == "0"
assert solution.addBinary("1111", "1111") == "11110"


