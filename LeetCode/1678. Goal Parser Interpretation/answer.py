# 1678. Goal Parser Interpretation
# https://leetcode.com/problems/goal-parser-interpretation/

class Solution:
    def interpret(self, command: str) -> str:
        result = ""
        tmp = ""
        parser_table = {'G': 'G', '()': 'o', '(al)': 'al'}
        for str in command:
            tmp += str
            if tmp in parser_table:
                result += parser_table[tmp]
                tmp = ""

        return result