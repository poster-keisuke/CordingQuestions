# 2829. Determine the Minimum Sum of a k-avoiding Array
# https://leetcode.com/problems/determine-the-minimum-sum-of-a-k-avoiding-array/

class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        st = set()
        result = 0
        i = 1

        while len(st) < n:
            if k - i not in st:
                st.add(i)
                result += i

            i += 1

        return result
