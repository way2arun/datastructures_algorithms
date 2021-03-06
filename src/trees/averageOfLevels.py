"""
Average of Levels in Binary Tree
Given a non-empty binary tree, return the average value of the nodes on each level in the form of an array.
Example 1:
Input:
    3
   / \
  9  20
    /  \
   15   7
Output: [3, 14.5, 11]
Explanation:
The average value of nodes on level 0 is 3,  on level 1 is 14.5, and on level 2 is 11. Hence return [3, 14.5, 11].
Note:
The range of node's value is in the range of 32-bit signed integer.
"""


# Definition for a binary tree node.
from typing import List


class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        # Solution 1 - 52 ms
        """"
        result = []
        level = (root,)
        while level:
            result.append(sum(node.val for node in level) / len(level))
            level = tuple(leaf for node in level for leaf in (node.left, node.right) if leaf)

        return result
        """
        # Solution 2 - 32 ms
        queue = [root]
        answer = []

        while queue:
            temp = []
            answer.append(self.Average(queue))

            for el in queue:
                if el.left != None:
                    temp.append(el.left)
                if el.right != None:
                    temp.append(el.right)
            queue = temp

        return answer

    def Average(self, queue):
        total = 0
        n = 0

        for el in queue:
            total += el.val
            n += 1

        return float(total / n)


# Main Call
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

solution = Solution()
print(solution.averageOfLevels(root))