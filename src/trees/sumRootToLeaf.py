"""
 Sum of Root To Leaf Binary Numbers
 https://leetcode.com/explore/challenge/card/september-leetcoding-challenge/555/week-2-september-8th-september-14th/3453/
 Given a binary tree, each node has value 0 or 1.  Each root-to-leaf path represents a binary number starting with the most significant bit.  For example, if the path is 0 -> 1 -> 1 -> 0 -> 1, then this could represent 01101 in binary, which is 13.

For all leaves in the tree, consider the numbers represented by the path from the root to that leaf.

Return the sum of these numbers.



Example 1:



Input: [1,0,1,0,1,0,1]
Output: 22
Explanation: (100) + (101) + (110) + (111) = 4 + 5 + 6 + 7 = 22


Note:

The number of nodes in the tree is between 1 and 1000.
node.val is 0 or 1.
The answer will not exceed 2^31 - 1.
   Hide Hint #1
Find each path, then transform that path to an integer in base 10.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumRootToLeaf(self, root: TreeNode, value=0) -> int:
        # Solution 1 - 40 ms
        """
        self.res = 0
        self.traverse(root, '')
        return self.res
        """
        # Solution 2 - 20 ms
        """
                Same as previous solution, but you the fact that bits
                are base 2 to increment, rather than doing string conversion.
                Recursive DFS to save paths
        """

        self.total = 0
        self.DFS(root, 0)
        return int(self.total)

        # Solution 3 - 24 ms
        # Add parameter value = 0 in the sumRootToLeaf function
        """
        if not root:
            return 0
        value = (value << 1) + root.val
        if root.left == root.right:
            return value
        return self.sumRootToLeaf(root.right, value) + self.sumRootToLeaf(root.left, value)
        """

    def DFS(self, root, binary):
        if root is None:
            return
        binary = binary * 2 + root.val
        if root.left is None and root.right is None:
            self.total += binary
        else:
            self.DFS(root.left, binary)
            self.DFS(root.right, binary)

    def traverse(self, root, s):
        if root:
            s += str(root.val)
            if not root.left and not root.right:
                self.res += int(s, 2)  # Binary to Decimal Conversion and value addition
                return
            self.traverse(root.left, s)
            self.traverse(root.right, s)
        return


# Main Call
# Input: [1,0,1,0,1,0,1]
root = TreeNode(1)
root.left = TreeNode(0)
root.left.left = TreeNode(0)
root.left.right = TreeNode(1)
root.right = TreeNode(1)
root.right.left = TreeNode(0)
root.right.right = TreeNode(1)

solution = Solution()
print(solution.sumRootToLeaf(root))
