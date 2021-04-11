"""
Deepest Leaves Sum
Given the root of a binary tree, return the sum of values of its deepest leaves.


Example 1:


Input: root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
Output: 15
Example 2:

Input: root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
Output: 19


Constraints:

The number of nodes in the tree is in the range [1, 104].
1 <= Node.val <= 100
   Hide Hint #1
Traverse the tree to find the max depth.
   Hide Hint #2
Traverse the tree again to compute the sum required.
"""


# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        # Solution 1 - with BFS
        """
        q, ans, qlen, curr = [root], 0, 0, 0
        while len(q):
            qlen, ans = len(q), 0
            for _ in range(qlen):
                curr = q.pop(0)
                ans += curr.val
                if curr.left: q.append(curr.left)
                if curr.right: q.append(curr.right)
        return ans
        """
        # Solution 2 - with Recursive DFS - 88 ms
        """
        sums = []

        def dfs(node: TreeNode, lvl: int):
            if lvl == len(sums):
                sums.append(node.val)
            else:
                sums[lvl] += node.val
            if node.left: dfs(node.left, lvl + 1)
            if node.right: dfs(node.right, lvl + 1)

        dfs(root, 0)
        return sums[-1]
        """
        # Solution 3 - 64 ms
        queue = [root]
        while 1:
            next_queue = list()
            for node in queue:
                if node.left:
                    next_queue.append(node.left)
                if node.right:
                    next_queue.append(node.right)
            if next_queue:
                queue = next_queue
            else:
                return sum(map(lambda x: x.val, queue))



# Main Call
root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.left.left.left = TreeNode(7)

root.right = TreeNode(3)
root.right.right = TreeNode(6)
root.right.right.right = TreeNode(8)


solution = Solution()
print(solution.deepestLeavesSum(root))