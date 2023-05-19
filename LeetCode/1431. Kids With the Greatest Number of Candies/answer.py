# 1431. Kids With the Greatest Number of Candies
# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        # Initialize max_count
        max_count = 0
        for candie in candies:
            if max_count < candie:
                max_count = candie

        results = []

        for i in range(len(candies)):
            candies[i] = candies[i] + extraCandies
            if candies[i] >= max_count:
                results.append(True)
            else:
                results.append(False)

        return results