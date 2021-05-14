"""
Flatten Binary Tree to Linked List
Given the root of a binary tree, flatten the tree into a "linked list":

The "linked list" should use the same TreeNode class where the right child pointer points to the next node in the list and the left child pointer is always null.
The "linked list" should be in the same order as a pre-order traversal of the binary tree.


Example 1:


Input: root = [1,2,5,3,4,null,6]
Output: [1,null,2,null,3,null,4,null,5,null,6]
Example 2:

Input: root = []
Output: []
Example 3:

Input: root = [0]
Output: [0]


Constraints:

The number of nodes in the tree is in the range [0, 2000].
-100 <= Node.val <= 100


Follow up: Can you flatten the tree in-place (with O(1) extra space)?
   Hide Hint #1
If you notice carefully in the flattened tree, each node's right child points to the next node of a pre-order traversal.
"""

from src.trees.printBinaryTree import PrintBinaryTree
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # Solution 1 - 44 ms
        """
        head, curr = None, root
        while head != root:
            if curr.right == head:
                curr.right = None
            if curr.left == head:
                curr.left = None
            if curr.right:
                curr = curr.right
            elif curr.left:
                curr = curr.left
            else:
                curr.right, head, curr = head, curr, root

        print_tree = PrintBinaryTree()
        response = print_tree.print_tree(root)
        print(response)
        """
        # Solution 2 - 12 ms
        cur = root
        while cur:
            if cur.left:
                self.flatten(cur.left)
                left_tail = cur.left
                while left_tail.right:
                    left_tail = left_tail.right
                old_right = cur.right
                cur.right = cur.left
                cur.left = None
                left_tail.right = old_right
                left_tail.left = None
                cur = old_right
            else:
                cur = cur.right

        print_tree = PrintBinaryTree()
        response = print_tree.print_tree(root)
        print(response)


# Main Call
root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right = TreeNode(5)
root.right.right = TreeNode(6)

solution = Solution()
solution.flatten(root)
