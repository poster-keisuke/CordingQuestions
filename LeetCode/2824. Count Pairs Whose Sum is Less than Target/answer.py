# 2824. Count Pairs Whose Sum is Less than Target
# https://leetcode.com/problems/count-pairs-with-sum-is-less-than-target/

class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        count = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i < j and nums[i] + nums[j] < target:
                    count += 1

        return count
