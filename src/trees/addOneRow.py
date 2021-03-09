"""
Add One Row to Tree
Given the root of a binary tree, then value v and depth d, you need to add a row of nodes with value v at the given depth d. The root node is at depth 1.

The adding rule is: given a positive integer depth d, for each NOT null tree nodes N in depth d-1, create two tree nodes with value v as N's left subtree root and right subtree root. And N's original left subtree should be the left subtree of the new left subtree root, its original right subtree should be the right subtree of the new right subtree root. If depth d is 1 that means there is no depth d-1 at all, then create a tree node with value v as the new root of the whole original tree, and the original tree is the new root's left subtree.

Example 1:
Input:
A binary tree as following:
       4
     /   \
    2     6
   / \   /
  3   1 5

v = 1

d = 2

Output:
       4
      / \
     1   1
    /     \
   2       6
  / \     /
 3   1   5

Example 2:
Input:
A binary tree as following:
      4
     /
    2
   / \
  3   1

v = 1

d = 3

Output:
      4
     /
    2
   / \
  1   1
 /     \
3       1
Note:
The given d is in range [1, maximum depth of the given tree + 1].
The given binary tree has at least one tree node.
"""

from src.trees.printBinaryTree import PrintBinaryTree

# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        # Solution 1 - 48 ms
        """
        dummy = TreeNode(0, root, None)
        row = [dummy]
        for _ in range(1, d):
            row = [child for node in row if node for child in (node.left, node.right) if child]

        for node in row:
            node.left = TreeNode(v, left=node.left)
            node.right = TreeNode(v, right=node.right)

        return dummy.left
        """
        # Solution 2 - 36 ms
        dep = 1
        stack = []
        stack.append(root)
        if d == 1:
            new_node = TreeNode(v)
            new_node.left = root
            root = new_node
        while dep < d:
            if dep == d - 1:

                for i in range(len(stack)):
                    new_nodel = TreeNode(v)
                    new_noder = TreeNode(v)
                    if stack[i].left:
                        left = stack[i].left
                    else:
                        left = None
                    if stack[i].right:
                        right = stack[i].right
                    else:
                        right = None
                    stack[i].left = new_nodel
                    stack[i].right = new_noder
                    new_nodel.left = left

                    new_noder.right = right
                break

            p = []
            while len(stack) != 0:
                u = stack.pop()
                if u.left:
                    p.append(u.left)
                if u.right:
                    p.append(u.right)
            stack = p
            dep += 1
        return root


# Main Call
root = TreeNode(4)
root.left = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(1)
root.right = TreeNode(6)
root.right.left = TreeNode(5)


v = 1
d = 2

solution = Solution()
result = solution.addOneRow(root, v, d)
# Lets print the binary tree
print_tree = PrintBinaryTree()
response = print_tree.print_tree(result)
print(response)