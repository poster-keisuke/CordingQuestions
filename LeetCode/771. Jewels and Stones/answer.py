# 771. Jewels and Stones
# https://leetcode.com/problems/jewels-and-stones/

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewels_map = {}
        for i in range(len(jewels)):
            jewels_map[jewels[i]] = jewels[i]

        match = 0
        for j in range(len(stones)):
            if stones[j] in jewels_map:
                match += 1

        return match