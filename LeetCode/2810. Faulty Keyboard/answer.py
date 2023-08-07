# 2810. Faulty Keyboard
# https://leetcode.com/problems/faulty-keyboard/

class Solution:
    def finalString(self, s: str) -> str:
        result = ""

        for c in s:
            if c == "i":
                result = result[::-1]
            else:
                result += c

        return result
