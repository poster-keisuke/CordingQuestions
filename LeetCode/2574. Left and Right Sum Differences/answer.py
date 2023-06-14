# 2574. Left and Right Sum Differences
# https://leetcode.com/problems/left-and-right-sum-differences/

class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        # create left sum
        left_sum = [0]
        for i in range(0, len(nums)-1):
            left_sum.append(nums[i] + left_sum[i])

        # create right sum
        right_sum = [0]
        for i in range(len(nums)-1, 0, -1):
            right_sum.insert(0, nums[i] + right_sum[0])

        # create answer sum
        results = []
        for i in range(len(left_sum)):
            results.append(abs(left_sum[i]-right_sum[i]))

        return results