# 1769. Minimum Number of Operations to Move All Balls to Each Box
# https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/

class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        result = [0] * len(boxes)
        left_count,left_cost = 0, 0
        for i in range(1,len(boxes)):
            if boxes[i-1] == '1':
                left_count += 1
            left_cost += left_count
            result[i] = left_cost

        right_count,right_cost = 0, 0
        for i in range(len(boxes)-2, -1, -1):
            if boxes[i+1] == '1':
                right_count += 1
            right_cost += right_count
            result[i] += right_cost

        return result

