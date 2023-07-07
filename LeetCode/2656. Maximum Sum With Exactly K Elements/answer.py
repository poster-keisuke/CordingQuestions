# 2656. Maximum Sum With Exactly K Elements
# https://leetcode-cn.com/problems/maximum-sum-with-exactly-k-elements/

class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        sorted_nums = sorted(nums)
        score = 0

        while k > 0:
            k -= 1
            max_idx = len(sorted_nums)-1
            score += sorted_nums[max_idx]
            sorted_nums[max_idx] += 1

        return score
