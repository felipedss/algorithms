# Leetcode: https://leetcode.com/problems/valid-parentheses

class Solution(object):

    def isValid(self, text):
        self.stack = []
        for character in text:
            if character == "(" or character == "[" or character == "{":
                self.stack.append(character)
            else:
                if len(self.stack) == 0:
                    return False
                
                top = self.stack.pop(len(self.stack) -1)
                print(top)
                if (top == "(" and character != ")") or (top == "[" and character != "]")  or (top == "{" and character != "}"):
                    return False

        return len(self.stack) == 0
                
            
solution = Solution() 
assert solution.isValid("()"), "Should be valid"
assert not solution.isValid("(]"), "Should not be valid"
assert solution.isValid("()[]()"), "Should be valid"
assert solution.isValid("()()([[]])[]()"), "Should be valid"
assert not solution.isValid("()()([([)]])[]()"), "Should be valid"