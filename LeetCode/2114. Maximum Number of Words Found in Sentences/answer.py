# 2114. Maximum Number of Words Found in Sentences
# https://leetcode.com/problems/maximum-number-of-words-found-in-sentences/

class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        max_count = 0
        for i in range(len(sentences)):
            count = 1
            for j in range(len(sentences[i])):
                if sentences[i][j] == " ":
                    count += 1
            if max_count < count:
                max_count = count
        return max_count