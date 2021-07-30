#  9. Palindrome Number
#  https://leetcode.com/problems/palindrome-number/

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        if 0 < x <= 9: return True

        original = x
        num = x
        reverse = 0

        for i in str(x):
            tmp = num % 10
            num = num // 10

            reverse = reverse * 10 + tmp

        return reverse == original
