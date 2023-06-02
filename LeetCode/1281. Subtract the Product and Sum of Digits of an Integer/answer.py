# 1281. Subtract the Product and Sum of Digits of an Integer
# https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        num_str = str(n)
        product = 1
        sum = 0

        for i in range(len(num_str)):
            product *= int(num_str[i])
            sum += int(num_str[i])

        return product - sum