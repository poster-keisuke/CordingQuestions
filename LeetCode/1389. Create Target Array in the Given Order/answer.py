# 1389. Create Target Array in the Given Order
# https://leetcode.com/problems/create-target-array-in-the-given-order/

class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        num_map = {}
        for i in range(len(nums)):
            num_map[i] = nums[i]
        results = []
        for i in range(len(index)):
            results.insert(index[i], num_map[i])
        return results