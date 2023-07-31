# 2788. Split Strings by Separator
# https://leetcode.com/problems/split-strings-by-separator/

class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        text = separator.join(words)
        return filter(lambda x: x != "", text.split(separator))
