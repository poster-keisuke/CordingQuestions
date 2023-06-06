# 2160. Minimum Sum of Four Digit Number After Splitting Digits
# https://leetcode.com/problems/minimum-sum-of-four-digit-number-after-splitting-digits/

class Solution:
    def minimumSum(self, num: int) -> int:
        sorted_num = sorted(str(num))

        result_1 = 0
        result_2 = 0
        for i in range(0, int(len(sorted_num)/2)):
            if i == 0:
                result_1 += int(sorted_num[i*2]) * 10
                result_2 += int(sorted_num[(i*2)+1]) * 10
            else:
                result_1 += int(sorted_num[i*2])
                result_2 += int(sorted_num[(i*2)+1])

        return result_1 + result_2
