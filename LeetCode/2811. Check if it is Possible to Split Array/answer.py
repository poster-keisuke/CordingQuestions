# 2811. Check if it is Possible to Split Array
# https://leetcode-cn.com/problems/check-if-it-is-possible-to-split-array/

class Solution:
    def canSplitArray(self, nums: List[int], m: int) -> bool:
        for i in range(len(nums)-1):
            if nums[i] + nums[i+1] >= m:
                return True
        return len(nums) <= 2