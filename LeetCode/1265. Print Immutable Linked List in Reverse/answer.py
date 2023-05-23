# 1265. Print Immutable Linked List in Reverse
# https://leetcode.com/problems/print-immutable-linked-list-in-reverse/

# """
# This is the ImmutableListNode's API interface.
# You should not implement it, or speculate about its implementation.
# """
# class ImmutableListNode:
#     def printValue(self) -> None: # print the value of this node.
#     def getNext(self) -> 'ImmutableListNode': # return the next node.

class Solution:
    def printLinkedListInReverse(self, head: 'ImmutableListNode') -> None:
        next_node = head
        nodes = []
        while next_node is not None:
            nodes.append(next_node)
            next_node = next_node.getNext()

        for i in range(len(nodes), 0, -1):
            nodes[i-1].printValue()