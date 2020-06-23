"""
https://leetcode.com/explore/challenge/card/june-leetcoding-challenge/542/week-4-june-22nd-june-28th/3369/
Given a complete binary tree, count the number of nodes.

Note:

Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

Example:

Input:
    1
   / \
  2   3
 / \  /
4  5 6

Output: 6
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countNodes(self, root: TreeNode) -> int:
        # Solution 1 - 88 ms
        """
        if not root:
            return 0
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
        """

        # Solution 2 - 60 ms
        def find_value(value):
            stack = []
            while value > 1:
                stack.append(value % 2)
                value //= 2
            # print(stack)
            current = root
            while stack:
                direction = stack.pop()
                if direction == 0:
                    if current.left:
                        current = current.left
                    else:
                        return False
                else:
                    if current.right:
                        current = current.right
                    else:
                        return False
            return True

        def find_depth(node):
            if not node:
                return 0
            return 1 + find_depth(node.left)

        depth = find_depth(root)
        if depth == 0:
            return 0
        left, right = 2 ** (depth - 1), (2 ** depth) - 1
        # print(left)
        # print(right)
        #         print(find_value(4))
        #         print(find_value(5))
        #         print(find_value(6))
        #         print(find_value(7))

        while left <= right:
            mid = (left + right) // 2
            if find_value(mid):
                left = mid + 1
            else:
                right = mid - 1
        return left - 1


# Main Call
tree_root = TreeNode(1)
tree_left_1 = TreeNode(2)
tree_right_1 = TreeNode(3)
tree_left_2 = TreeNode(4)
tree_left_3 = TreeNode(5)
tree_right_left_4 = TreeNode(6)

tree_root.left = tree_left_1
tree_left_1.left = tree_left_2
tree_left_1.right = tree_left_3
tree_root.right = tree_right_1
tree_right_1.left = tree_right_left_4

tree_right_1.right = None
tree_left_2.left = None
tree_left_2.right = None
tree_left_3.left = None
tree_left_3.right = None

solution = Solution()
print(solution.countNodes(tree_root))
