# 1874. Minimize Product Sum of Two Arrays
# https://leetcode.com/problems/minimize-product-sum-of-two-arrays/

class Solution:
    def minProductSum(self, nums1: List[int], nums2: List[int]) -> int:
        # sort as desc
        nums1.sort()
        # sort as asc
        nums2.sort(reverse=True)

        nums1_map = {}
        for i in range(len(nums1)):
            nums1_map[i] = nums1[i]

        result = 0
        for i in range(len(nums2)):
            result += nums1_map[i] * nums2[i]

        return result