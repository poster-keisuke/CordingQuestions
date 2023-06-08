# 1313. Decompress Run-Length Encoded List
# https://leetcode.com/problems/decompress-run-length-encoded-list/

# Brute Force Answer
class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(0, len(nums), 2):
            for j in range(nums[i]):
                result.append(nums[i+1])
        return result



# Another Answer
class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(0, len(nums), 2):
            result += [nums[i+1]] * nums[i]

        return result