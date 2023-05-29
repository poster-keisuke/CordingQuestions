# 1480. Running Sum of 1d Array
# https://leetcode.com/problems/running-sum-of-1d-array/

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        results = nums
        for i in range(1, len(nums)):
            results[i] = nums[i] + results[i-1]
        return results
