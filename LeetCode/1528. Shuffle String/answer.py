# 1528. Shuffle String
# https://leetcode.com/problems/shuffle-string/

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        s_map = {}
        result = ""
        sorted_indices = sorted(indices)

        for i in range(len(indices)):
            s_map[indices[i]] = s[i]

        for i in sorted_indices:
            result += s_map[i]

        return result
