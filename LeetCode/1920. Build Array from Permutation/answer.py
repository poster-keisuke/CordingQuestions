# 1920. Build Array from Permutation
# https://leetcode.com/problems/build-array-from-permutation/


class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        nums_map = {}
        for i in range(len(nums)):
            nums_map[i] = nums[nums[i]]

        ans = []
        for j in range(len(nums)):
            ans.append(nums_map[j])

        return ans