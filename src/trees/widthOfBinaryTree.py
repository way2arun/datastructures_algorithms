"""
https://leetcode.com/explore/challenge/card/july-leetcoding-challenge/545/week-2-july-8th-july-14th/3385/
Given a binary tree, write a function to get the maximum width of the given tree. The width of a tree is the maximum width among all levels. The binary tree has the same structure as a full binary tree, but some nodes are null.

The width of one level is defined as the length between the end-nodes (the leftmost and right most non-null nodes in the level, where the null nodes between the end-nodes are also counted into the length calculation.

Example 1:

Input:

           1
         /   \
        3     2
       / \     \
      5   3     9

Output: 4
Explanation: The maximum width existing in the third level with the length 4 (5,3,null,9).
Example 2:

Input:

          1
         /
        3
       / \
      5   3

Output: 2
Explanation: The maximum width existing in the third level with the length 2 (5,3).
Example 3:

Input:

          1
         / \
        3   2
       /
      5

Output: 2
Explanation: The maximum width existing in the second level with the length 2 (3,2).
Example 4:

Input:

          1
         / \
        3   2
       /     \
      5       9
     /         \
    6           7
Output: 8
Explanation:The maximum width existing in the fourth level with the length 8 (6,null,null,null,null,null,null,7).


Note: Answer will in the range of 32-bit signed integer.
"""
# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        # Solution 1 - 44 ms
        """
        traversal_queue = [(root, 1)] if root else []
        max_width = 0

        # launch level-order traversal
        while traversal_queue:
            next_level_queue = []
            # record for first serial and last serial for each level
            first_serial, last_serial = None, None
            for node, serial_number in traversal_queue:
                if node and not first_serial:
                    first_serial = serial_number
                if node:
                    last_serial = serial_number
                    if node.left:
                        next_level_queue.append((node.left, 2 * serial_number))
                    if node.right:
                        next_level_queue.append((node.right, 2 * serial_number + 1))
            cur_width = last_serial - first_serial + 1
            # update max width for current level
            max_width = max(max_width, cur_width)
            # update traversal queue for next level
            traversal_queue = next_level_queue
        return max_width
        """
        # Solution 2 - 20 ms
        q = []
        mx = 0
        q.append([root, 0])
        while q:
            ll = len(q)
            _, lhi = q[0]
            for i in range(ll):
                tmp, cid = q.pop(0)
                if tmp.left:
                    q.append([tmp.left, 2 * cid])
                if tmp.right:
                    q.append([tmp.right, 2 * cid + 1])
            mx = max(mx, cid - lhi + 1)
        return mx


# Main Call
root = TreeNode(1)
root.left = TreeNode(3)
root.right = TreeNode(2)
root.left.left = TreeNode(5)
root.right.right = TreeNode(9)
root.left.left.left = TreeNode(6)
root.right.right.right = TreeNode(7)

solution = Solution()
print(solution.widthOfBinaryTree(root))
