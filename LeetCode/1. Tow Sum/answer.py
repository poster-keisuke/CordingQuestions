# 1. Two Sum
# https://leetcode.com/problems/two-sum/

class BruteForceSolution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] + nums[j] == target and i != j:
                    return [i, j]
        return [-1, -1]


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        comp = {}
        for i in range(len(nums)):
            if target - nums[i] in comp:
                return [comp[target - nums[i]], i]
            comp[nums[i]] = i

        return []