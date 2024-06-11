class Solution:
    def isValid(self, s):
        """Leetcode"""

        stack = []
        lookup = {
            "}": "{",
            ")": "(",
            "]": "["
        }

        for symbol in s:
            if symbol in lookup.values():
                stack.append(symbol)
            elif stack and lookup[symbol] == stack[-1]:
                stack.pop()
            else:
                return False

        return stack == []


solution = Solution()
print(solution.isValid("()([{}])"))
