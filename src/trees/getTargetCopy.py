"""
Find a Corresponding Node of a Binary Tree in a Clone of That Tree
Given two binary trees original and cloned and given a reference to a node target in the original tree.

The cloned tree is a copy of the original tree.

Return a reference to the same node in the cloned tree.

Note that you are not allowed to change any of the two trees or the target node and the answer must be a reference to a node in the cloned tree.

Follow up: Solve the problem if repeated values on the tree are allowed.



Example 1:


Input: tree = [7,4,3,null,null,6,19], target = 3
Output: 3
Explanation: In all examples the original and cloned trees are shown. The target node is a green node from the original tree. The answer is the yellow node from the cloned tree.
Example 2:


Input: tree = [7], target =  7
Output: 7
Example 3:


Input: tree = [8,null,6,null,5,null,4,null,3,null,2,null,1], target = 4
Output: 4
Example 4:


Input: tree = [1,2,3,4,5,6,7,8,9,10], target = 5
Output: 5
Example 5:


Input: tree = [1,2,null,3], target = 2
Output: 2


Constraints:

The number of nodes in the tree is in the range [1, 10^4].
The values of the nodes of the tree are unique.
target node is a node from the original tree and is not null.
"""

from src.trees.printBinaryTree import PrintBinaryTree


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        # Solution 1 - 680 ms
        """
        def dfs(node):
            if not node:
                return False
            if node == target:
                return True
            L, R = dfs(node.left), dfs(node.right)
            if L or R:
                self.path += [0] if L else [1]
            return L or R

        self.path = []
        dfs(original)
        for i in self.path[::-1]:
            cloned = cloned.left if i == 0 else cloned.right

        return cloned
        """
        # Solution 2 - 568 ms
        if not original:
            return None
        if original == target:
            return cloned
        L = self.getTargetCopy(original.left, cloned.left, target)
        if L:
            return L
        return self.getTargetCopy(original.right, cloned.right, target)


# Main Call
original = TreeNode(7)
original.left = TreeNode(4)
original.right = TreeNode(3)
original.right.left = TreeNode(6)
original.right.right = TreeNode(19)

cloned = TreeNode(7)
cloned.left = TreeNode(4)
cloned.right = TreeNode(3)
cloned.right.left = TreeNode(6)
cloned.right.right = TreeNode(19)

target = TreeNode(3)

solution = Solution()
node = solution.getTargetCopy(original, cloned, target)
print(node)
# Lets print the binary tree
if node is not None:
    print_tree = PrintBinaryTree()
    response = print_tree.print_tree(node)
    print(response)
