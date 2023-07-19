# 2535. Difference Between Element Sum and Digit Sum of an Array
# https://leetcode.com/problems/difference-between-element-sum-and-digit-sum-of-an-array/

class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        num_sum, digit_sum = 0, 0
        digits = []

        for num in nums:
            num_sum += num

            while num > 0:
                digits.append(num%10)
                num //= 10

        for digit in digits:
            digit_sum += digit

        return abs(num_sum - digit_sum)