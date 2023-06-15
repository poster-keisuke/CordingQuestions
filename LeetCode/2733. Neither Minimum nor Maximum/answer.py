# 2733. Neither Minimum nor Maximum
# https://leetcode.com/problems/neither-minimum-nor-maximum/

class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        if (len(nums)) < 3: return -1

        min_num = min(nums)
        max_num = max(nums)

        for i in range(len(nums)):
            if nums[i] != min_num and nums[i] != max_num:
                return nums[i]

        return -1