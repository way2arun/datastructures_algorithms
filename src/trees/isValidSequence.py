"""
Given a binary tree where each path going from the root to any leaf form a valid sequence, check if a given string is a valid sequence in such binary tree.

We get the given string from the concatenation of an array of integers arr and the concatenation of all values of the nodes along a path results in a sequence in the given binary tree.



Example 1:



Input: root = [0,1,0,0,1,0,null,null,1,0,0], arr = [0,1,0,1]
Output: true
Explanation:
The path 0 -> 1 -> 0 -> 1 is a valid sequence (green color in the figure).
Other valid sequences are:
0 -> 1 -> 1 -> 0
0 -> 0 -> 0
Example 2:



Input: root = [0,1,0,0,1,0,null,null,1,0,0], arr = [0,0,1]
Output: false
Explanation: The path 0 -> 0 -> 1 does not exist, therefore it is not even a sequence.
Example 3:



Input: root = [0,1,0,0,1,0,null,null,1,0,0], arr = [0,1,1]
Output: false
Explanation: The path 0 -> 1 -> 1 is a sequence, but it is not a valid sequence.


Constraints:

1 <= arr.length <= 5000
0 <= arr[i] <= 9
Each node's value is between [0 - 9].
   Hide Hint #1
Depth-first search (DFS) with the parameters: current node in the binary tree and current position in the array of integers.
   Hide Hint #2
When reaching at final position check if it is a leaf node.

https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/532/week-5/3315/
"""

# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidSequence(self, root: TreeNode, arr: List[int]) -> bool:
        # 112 ms
        counter = 0
        return self.traverse_path(root, arr, counter, len(arr))

    def traverse_path(self, root, arr, counter, array_length):
        if not root:
            return array_length == 0
        if root.left is None and root.right is None:
            if counter == array_length - 1:
                if root.val == arr[counter]:
                    return True

        if counter < array_length:
            if root.val == arr[counter]:
                return self.traverse_path(root.left, arr, counter + 1, array_length) or self.traverse_path(root.right,
                                                                                                           arr,
                                                                                                           counter + 1,
                                                                                                           array_length)


# Main Call
root = TreeNode(0)
root.left = TreeNode(1)
root.right = TreeNode(0)
root.left.left = TreeNode(0)
root.left.left.right = TreeNode(1)
root.left.right = TreeNode(1)
root.left.right.left = TreeNode(0)
root.left.right.right = TreeNode(0)
root.right.right = None
root.right.left = TreeNode(0)

arr = [0, 1, 0, 1]

solution = Solution()
print(solution.isValidSequence(root, arr))
