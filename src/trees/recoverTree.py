"""
Recover Binary Search Tree
You are given the root of a binary search tree (BST), where exactly two nodes of the tree were swapped by mistake. Recover the tree without changing its structure.

Follow up: A solution using O(n) space is pretty straight forward. Could you devise a constant space solution?



Example 1:


Input: root = [1,3,null,null,2]
Output: [3,1,null,null,2]
Explanation: 3 cannot be a left child of 1 because 3 > 1. Swapping 1 and 3 makes the BST valid.
Example 2:


Input: root = [3,1,4,null,null,2]
Output: [2,1,4,null,null,3]
Explanation: 2 cannot be in the right subtree of 3 because 2 < 3. Swapping 2 and 3 makes the BST valid.


Constraints:

The number of nodes in the tree is in the range [2, 1000].
-231 <= Node.val <= 231 - 1
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # Solution 1 - 52 ms

        if not root:
            return

        stack = []
        self.addLeftNodes(stack, root)
        prev = None
        swapNodes = [None, None]

        while stack:
            node = stack.pop()
            if prev and node.val < prev.val:
                swapNodes[0] = node
                if swapNodes[1] is None:
                    swapNodes[1] = prev
                else:
                    break
            prev = node
            self.addLeftNodes(stack, node.right)

        swapNodes[0].val, swapNodes[1].val = swapNodes[1].val, swapNodes[0].val

        # Solution 2 - 56 ms
        """
        x = y = prev = pred = None
        while root:
            if root.left:
                prev = root.left
                while prev.right and prev.right != root:
                    prev = prev.right
                if prev.right is None:
                    prev.right = root
                    root = root.left
                else:
                    if pred and root.val < pred.val:
                        y = root
                        if x == None:
                            x = pred
                    pred = root
                    prev.right = None
                    root = root.right
            else:
                if pred and root.val < pred.val:
                    y = root
                    if x == None:
                        x = pred
                pred = root
                root = root.right
        x.val, y.val = y.val, x.val
        return x
        """

    def addLeftNodes(self, stack, root):
        while root:
            stack.append(root)
            root = root.left


# Main Call
tree_root = TreeNode(1)
tree_root.left = TreeNode(3)
tree_root.left.right = TreeNode(2)

solution = Solution()
solution.recoverTree(tree_root)
