# 2011. Final Value of Variable After Performing Operations
# https://leetcode.com/problems/final-value-of-variable-after-performing-operations/

class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        value = 0
        for i in range(len(operations)):
            match operations[i]:
                case "X++" | "++X":
                    value += 1
                    continue
                case "X--" | "--X":
                    value -= 1
                    continue
        return value

