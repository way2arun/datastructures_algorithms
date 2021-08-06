"""
N-ary Tree Level Order Traversal
Given an n-ary tree, return the level order traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).



Example 1:



Input: root = [1,null,3,2,4,null,5,6]
Output: [[1],[3,2,4],[5,6]]
Example 2:



Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
Output: [[1],[2,3,4,5],[6,7,8,9,10],[11,12,13],[14]]


Constraints:

The height of the n-ary tree is less than or equal to 1000
The total number of nodes is between [0, 104]
"""

# Definition for a Node.
from collections import deque
from typing import List


class Node:
    def __init__(self, val=None, child=None):
        self.val = val
        self.children = []
        if child is not None:
            for value in child:
                self.children.append(value)


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        # Solution 1 - 52 ms
        """
        if root is None: return []
        q = deque([root])
        ans = []
        while q:
            level = []
            for _ in range(len(q)):
                curr = q.popleft()
                level.append(curr.val)
                for child in curr.children:
                    q.append(child)
            ans.append(level)
        return ans
        """
        # Solution 2 - 32 ms
        if root is None:
            return []
        res = []
        stack = deque([root])
        while stack:
            cur = len(stack)
            temp = []
            while cur > 0:
                cur -= 1
                node = stack.popleft()
                temp.append(node.val)
                if node.children:
                    for children in node.children:
                        stack.append(children)
            res.append(temp)
        return res


# Main Call

node6 = Node(6)
node5 = Node(5)
node4 = Node(4)
node3 = Node(2)
node2 = Node(3, [node5, node6])
node1 = Node(1, [node2, node3, node4])
root = node1

solution = Solution()
print(solution.levelOrder(root))
