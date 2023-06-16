# 1512. Number of Good Pairs
# https://leetcode.com/problems/number-of-good-pairs/

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        repeat = {}
        count = 0

        for num in nums:
            if num in repeat:
                count += repeat[num]
                repeat[num] += 1
            else:
                repeat[num] = 1
        return count