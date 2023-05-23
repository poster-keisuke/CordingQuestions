# 1119. Remove Vowels from a String
# https://leetcode.com/problems/remove-vowels-from-a-string/

class Solution:
    def removeVowels(self, s: str) -> str:
        result = ""
        vowels = {"a": "a", "i": "i", "u": "u", "e": "e", "o": "o"}
        for char in s:
            if char not in vowels:
                result += char
        return result
