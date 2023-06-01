# 1365. How Many Numbers Are Smaller Than the Current Number
# https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

import copy

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        map = {}
        copy_nums = copy.copy(nums)
        copy_nums.sort()

        for i in range(len(nums)):
            if copy_nums[i] not in map:
                map[copy_nums[i]] = i

        for j in range(len(nums)):
            copy_nums[j] = map[nums[j]]

        return copy_nums
