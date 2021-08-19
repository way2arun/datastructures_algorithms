"""
Maximum Product of Splitted Binary Tree
Given the root of a binary tree, split the binary tree into two subtrees by removing one edge such that the product of the sums of the subtrees is maximized.

Return the maximum product of the sums of the two subtrees. Since the answer may be too large, return it modulo 109 + 7.

Note that you need to maximize the answer before taking the mod and not after taking it.



Example 1:


Input: root = [1,2,3,4,5,6]
Output: 110
Explanation: Remove the red edge and get 2 binary trees with sum 11 and 10. Their product is 110 (11*10)
Example 2:


Input: root = [1,null,2,3,4,null,null,5,6]
Output: 90
Explanation: Remove the red edge and get 2 binary trees with sum 15 and 6.Their product is 90 (15*6)
Example 3:

Input: root = [2,3,9,10,7,8,6,5,4,11,1]
Output: 1025
Example 4:

Input: root = [1,1]
Output: 1


Constraints:

The number of nodes in the tree is in the range [2, 5 * 104].
1 <= Node.val <= 104
   Hide Hint #1
If we know the sum of a subtree, the answer is max( (total_sum - subtree_sum) * subtree_sum) in each node.
"""


# Definition for a binary tree node.
from bisect import bisect_left


class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def maxProduct(self, root: TreeNode) -> int:
        # Solution 1 - 300 ms
        """
        def dfs(node):
            if not node: return 0
            ans = dfs(node.left) + dfs(node.right) + node.val
            res.append(ans)
            return ans

        res = []
        dfs(root)
        sum_all = max(res)
        return max(i * (sum_all - i) for i in res) % (10 ** 9 + 7)
        """
        # Solution 2 - 280 ms
        sub_sums = []

        def check_next(node: TreeNode):
            if node.left:
                check_next(node.left)
                node.val += node.left.val
            if node.right:
                check_next(node.right)
                node.val += node.right.val
            sub_sums.append(node.val)

        check_next(root)
        sub_sums.sort()
        tree_sum = sub_sums[-1]
        idx = bisect_left(sub_sums, tree_sum / 2)
        return (max((tree_sum - sub_sums[idx]) * sub_sums[idx],
                    (tree_sum - sub_sums[idx - 1]) * sub_sums[idx - 1])
                % 1_000_000_007)


# Main Call
root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right = TreeNode(3)
root.right.left = TreeNode(6)

solution = Solution()
print(solution.maxProduct(root))
