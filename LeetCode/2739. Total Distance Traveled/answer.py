# 2739. Total Distance Traveled
# https://leetcode.com/problems/total-distance-traveled/

class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        spare_tank = additionalTank
        remain_tank = mainTank
        distance = 0

        while remain_tank > 0:
            if remain_tank - 5 >= 0 and spare_tank > 0:
                distance += 5 * 10
                remain_tank -= 5
                remain_tank += 1
                spare_tank -= 1
            else:
                distance += remain_tank * 10
                remain_tank = 0

        return distance
