"""
All Elements in Two Binary Search Trees
https://leetcode.com/explore/challenge/card/september-leetcoding-challenge/554/week-1-september-1st-september-7th/3449/
Given two binary search trees root1 and root2.

Return a list containing all the integers from both trees sorted in ascending order.



Example 1:


Input: root1 = [2,1,4], root2 = [1,0,3]
Output: [0,1,1,2,3,4]
Example 2:

Input: root1 = [0,-10,10], root2 = [5,1,7,0,2]
Output: [-10,0,0,1,2,5,7,10]
Example 3:

Input: root1 = [], root2 = [5,1,7,0,2]
Output: [0,1,2,5,7]
Example 4:

Input: root1 = [0,-10,10], root2 = []
Output: [-10,0,10]
Example 5:


Input: root1 = [1,null,8], root2 = [8,1]
Output: [1,1,8,8]


Constraints:

Each tree has at most 5000 nodes.
Each node's value is between [-10^5, 10^5].
   Hide Hint #1
Traverse the first tree in list1 and the second tree in list2.
   Hide Hint #2
Merge the two trees in one list and sort it.
"""

# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        # Solution 1 - 364 ms
        """
        if root1 is None and root2 is None:
            return []

        result = []
        root1List = []
        root2List = []
        self.rootList(root1List, root1)
        self.rootList(root2List, root2)
        result = self.mergeList(root1List, root2List)
        return result

    def rootList(self, rList, root):
        if not root:
            return None

        self.rootList(rList, root.left)
        rList.append(root.val)
        self.rootList(rList, root.right)

    def mergeList(self, R1, R2):
        res = []
        i, j = 0, 0

        l1, l2 = len(R1), len(R2)

        while i < l1 and j < l2:
            if R1[i] < R2[j]:
                res.append(R1[i])
                i += 1
            else:
                res.append(R2[j])
                j += 1

        res = [*res, *R1[i:], *R2[j:]]
        return res
    """
        # Solution 2 - 316 ms
        l1, stack1, root = [], [], root1
        while stack1 or root:
            while root:
                stack1.append(root)
                root = root.left
            root = stack1.pop()
            l1.append(root.val)
            root = root.right
        l2, stack2, root = [], [], root2
        while stack2 or root:
            while root:
                stack2.append(root)
                root = root.left
            root = stack2.pop()
            l2.append(root.val)
            root = root.right
        l = l1 + l2
        return sorted(l)



# Main Call
root1 = TreeNode(2)
root1.left = TreeNode(1)
root1.right = TreeNode(4)

root2 = TreeNode(1)
root2.left = TreeNode(0)
root1.right = TreeNode(3)

solution = Solution()
print(solution.getAllElements(root1, root2))
