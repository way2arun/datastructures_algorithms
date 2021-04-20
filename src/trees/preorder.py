"""
N-ary Tree Preorder Traversal
Given the root of an n-ary tree, return the preorder traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal. Each group of children is separated by the null value (See examples)



Example 1:



Input: root = [1,null,3,2,4,null,5,6]
Output: [1,3,5,6,2,4]
Example 2:



Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
Output: [1,2,3,6,7,11,14,4,8,12,5,9,13,10]


Constraints:

The number of nodes in the tree is in the range [0, 104].
0 <= Node.val <= 104
The height of the n-ary tree is less than or equal to 1000.


Follow up: Recursive solution is trivial, could you do it iteratively?
"""

# Definition for a Node.
from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        # Solution 1 - 48 ms
        """
        if not root:
            return []
        stack, out = [root], []
        while stack:
            cur = stack.pop()
            out.append(cur.val)
            for child in cur.children[::-1]:
                stack += [child]
        return out
        """
        # Solution 2 - 32 ms
        if not root:
            return []
        L = [root.val]
        for c in root.children:
            if c:
                L += self.preorder(c)
        return L


# Main Call
# input nodes
        '''

          1
       /  |  \
      /   |   \
     2    3    4
    / \      / | \
   /   \    7  8  9
  5     6   
 /    / | \
10   11 12 13

        '''


root = Node(1)
left_child = Node(1,2)
left_child.children = Node(2,5)
left_child.children.children = Node(5,10)



"""
root = Node(1)
root.children.append(Node(3))
root.children.append(Node(4))
root.children[0].children.append(Node(5))
root.children[0].children[0].child.append(Node(10))
root.children[0].children.append(Node(6))
root.children[0].children[1].child.append(Node(11))
root.children[0].children[1].child.append(Node(12))
root.children[0].children[1].child.append(Node(13))
root.children[2].children.append(Node(7))
root.children[2].children.append(Node(8))
root.children[2].children.append(Node(9))
"""

solution = Solution()
print(solution.preorder(root))