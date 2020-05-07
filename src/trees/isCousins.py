"""
In a binary tree, the root node is at depth 0, and children of each depth k node are at depth k+1.

Two nodes of a binary tree are cousins if they have the same depth, but have different parents.

We are given the root of a binary tree with unique values, and the values x and y of two different nodes in the tree.

Return true if and only if the nodes corresponding to the values x and y are cousins.



Example 1:


Input: root = [1,2,3,4], x = 4, y = 3
Output: false
Example 2:


Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
Output: true
Example 3:



Input: root = [1,2,3,null,4], x = 2, y = 3
Output: false


Note:

The number of nodes in the tree will be between 2 and 100.
Each node has a unique integer value from 1 to 100.

https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/534/week-1-may-1st-may-7th/3322/

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        """
        # Solution 1 - 36 ms
        if root is None:
            return False
        x_node = self.depth_first_search(root, x, 0, root)
        print(x_node)
        y_node = self.depth_first_search(root, y, 0, root)
        print(y_node)
        print(x_node[0])
        print(y_node[0])

        print(x_node[1])
        print(y_node[1])

        return x_node[0] == y_node[0] and x_node[1] != y_node[1]

    def depth_first_search(self, tree_node, x, node_level, parent_node):
        if tree_node is None:
            return []
        if tree_node.val == x:
            return [node_level, parent_node.val]
        return self.depth_first_search(tree_node.left, x, node_level + 1, tree_node) + self.depth_first_search(tree_node.right, x, node_level + 1, tree_node)
    """
        # Solution 2
        self.x_node = []
        self.y_node = []
        if root:
            if root.val == x or root.val == y:
                return False
            self.traverse_tree(root, 1)
            print(self.x_node, self.y_node)
            if self.x_node[0] != self.y_node[0] and self.x_node[1] == self.y_node[1]:
                return True
        return False

    def traverse_tree(self, root, d):
        if root.left:
            if root.left.val == x:
                self.x_node.append(root.val)
                self.x_node.append(d + 1)
            if root.left.val == y:
                self.y_node.append(root.val)
                self.y_node.append(d + 1)
            self.traverse_tree(root.left, d + 1)
        if root.right:
            if root.right.val == x:
                self.x_node.append(root.val)
                self.x_node.append(d + 1)
            if root.right.val == y:
                self.y_node.append(root.val)
                self.y_node.append(d + 1)
            self.traverse_tree(root.right, d + 1)


# Main Call
# Initialize the Tree First
tree_root = TreeNode(1)
tree_root.left = TreeNode(2)
tree_root.left.left = TreeNode(4)
tree_root.left.right = None
tree_root.right = TreeNode(3)
tree_root.right.left = None
tree_root.right.right = None
x = 4
y = 3
solution = Solution()
response = solution.isCousins(tree_root, x, y)
print(response)

# second test case
tree_root = TreeNode(1)
tree_root.left = TreeNode(2)
tree_root.right = TreeNode(3)
tree_root.left.left = None
tree_root.left.right = TreeNode(4)
tree_root.right.left = None
tree_root.right.right = TreeNode(5)

x = 5
y = 4
solution = Solution()
response = solution.isCousins(tree_root, x, y)
print(response)
