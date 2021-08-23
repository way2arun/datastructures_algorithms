"""
Two Sum IV - Input is a BST
Given the root of a Binary Search Tree and a target number k, return true if there exist two elements in the BST such that their sum is equal to the given target.



Example 1:


Input: root = [5,3,6,2,4,null,7], k = 9
Output: true
Example 2:


Input: root = [5,3,6,2,4,null,7], k = 28
Output: false
Example 3:

Input: root = [2,1,3], k = 4
Output: true
Example 4:

Input: root = [2,1,3], k = 1
Output: false
Example 5:

Input: root = [2,1,3], k = 3
Output: true


Constraints:

The number of nodes in the tree is in the range [1, 104].
-104 <= Node.val <= 104
root is guaranteed to be a valid binary search tree.
-105 <= k <= 105
"""


# Definition for a binary tree node.
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        # Solution 1 - 84 ms
        """
        def pushLeft(st, root):
            while root:
                st.append(root)
                root = root.left

        def pushRight(st, root):
            while root:
                st.append(root)
                root = root.right

        def nextLeft(st):
            node = st.pop()
            pushLeft(st, node.right)
            return node.val

        def nextRight(st):
            node = st.pop()
            pushRight(st, node.left)
            return node.val

        stLeft, stRight = [], []
        pushLeft(stLeft, root)
        pushRight(stRight, root)

        left, right = nextLeft(stLeft), nextRight(stRight)
        while left < right:
            if left + right == k: return True
            if left + right < k:
                left = nextLeft(stLeft)
            else:
                right = nextRight(stRight)
        return False
        """
        # Solution 2 - 52 ms
        s = set()
        q = deque()
        q.append(root)
        # when q has elements on it, it will return True; otherwise, it's false.
        while q:
            temp = q.popleft()
            if temp.val in s:
                return True
            else:
                s.add(k - temp.val)
                if temp.left is not None:
                    q.append(temp.left)
                if temp.right is not None:
                    q.append(temp.right)
        return False


# Main Call
root = TreeNode(5)
root.left = TreeNode(3)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right = TreeNode(6)
root.right.right = TreeNode(7)
k = 9
solution = Solution()
print(solution.findTarget(root, k))
