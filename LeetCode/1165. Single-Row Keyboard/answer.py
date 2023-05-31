# 1165. Single-Row Keyboard
# https://leetcode.com/problems/single-row-keyboard/

class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        count = 0
        current_index = 0

        key_map = {}
        for i in range(len(keyboard)):
            key_map[keyboard[i]] = i

        for char in word:
            if char in key_map:
                count += abs(key_map[char] - current_index)
                current_index = key_map[char]
        return count