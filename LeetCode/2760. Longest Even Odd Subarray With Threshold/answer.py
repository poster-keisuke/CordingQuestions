# 2760. Longest Even Odd Subarray With Threshold
# https://leetcode-cn.com/problems/longest-even-odd-subarray-with-threshold/

class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        ans = 0
        i = 0
        last = float('inf')

        print(1-last)

        while i < len(nums):
            if nums[i] > threshold or (i > 0 and nums[i] % 2 == nums[i - 1] % 2):
                ans = max(ans, i - last)
                last = float('inf')
            if last == float('inf') and nums[i] <= threshold and nums[i] % 2 == 0:
                last = i
            i += 1

        ans = max(ans, i - last)
        return ans