"""
House Robber III
The thief has found himself a new place for his thievery again. There is only one entrance to this area, called the "root." Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that "all houses in this place forms a binary tree". It will automatically contact the police if two directly-linked houses were broken into on the same night.

Determine the maximum amount of money the thief can rob tonight without alerting the police.

Example 1:

Input: [3,2,3,null,3,null,1]

     3
    / \
   2   3
    \   \
     3   1

Output: 7
Explanation: Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.
Example 2:

Input: [3,4,5,1,3,null,1]

     3
    / \
   4   5
  / \   \
 1   3   1

Output: 9
Explanation: Maximum amount of money the thief can rob = 4 + 5 = 9.
"""


# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def rob(self, root: TreeNode) -> int:
        # Solution 1 - 44 ms
        """
        return max(self.check(root))
        """
        # Solution 2 - 24 ms
        def sub_rob(node):
            if not node:
                return (0, 0)
            l_child, l_grand_child = sub_rob(node.left)
            r_child, r_grand_child = sub_rob(node.right)

            child_profit = l_child + r_child
            grand_profit = node.val + l_grand_child + r_grand_child
            node_profit = max(child_profit, grand_profit)
            return (node_profit, l_child + r_child)

        return max(sub_rob(root))

    def check(self, root: TreeNode):
        if not root:
            return 0, 0

        not_rob_left, rob_left = self.check(root.left)
        not_rob_right, rob_right = self.check(root.right)

        # case 1: not rob cur
        case1 = max(
            not_rob_left + not_rob_right,
            rob_left + not_rob_right,
            not_rob_left + rob_right,
            rob_left + rob_right
        )

        # case2: rob cur one
        case2 = root.val + not_rob_left + not_rob_right

        return (case1, case2)


# Main Call
node = TreeNode(3)
node.left = TreeNode(4)
node.left.left = TreeNode(1)
node.left.right =  TreeNode(3)
node.right = TreeNode(5)
node.right.right = TreeNode(1)

solution = Solution()
print(solution.rob(node))