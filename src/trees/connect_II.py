"""
 Populating Next Right Pointers in Each Node II
Given a binary tree

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.



Follow up:

You may only use constant extra space.
Recursive approach is fine, you may assume implicit stack space does not count as extra space for this problem.


Example 1:



Input: root = [1,2,3,4,5,null,7]
Output: [1,#,2,3,#,4,5,7,#]
Explanation: Given the above binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.


Constraints:

The number of nodes in the given tree is less than 6000.
-100 <= node.val <= 100
"""

# Definition for a Node.
import collections

from src.trees.printBinaryTree import PrintBinaryTree


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        # Solution 1 - 40 ms
        """
        node = root
        while node:
            curr = dummy = Node(0)
            while node:
                if node.left:
                    curr.next = node.left
                    curr = curr.next
                if node.right:
                    curr.next = node.right
                    curr = curr.next
                node = node.next
            node = dummy.next

        return root
        """
        # Solution 2 - 24 ms
        if root is None:
            return root

        queue = collections.deque()
        queue.append(root)
        while queue:
            length = len(queue)
            pre = None
            for _ in range(length):
                node = queue.popleft()
                if pre is not None:
                    pre.next = node
                pre = node
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)

        return root


# Main Call
root = Node(1)
root.left = Node(2)
root.left.left = Node(4)
root.left.right = Node(5)
root.right = Node(3)
root.right.right = Node(7)
root.next = None
root.left.next = root.right.val
root.right.next = None
root.left.left.next = root.left.right.val
root.left.right.next = root.right.right.val
root.right.right.next = None

solution = Solution()
node = solution.connect(root)
# Lets print the binary tree
print_tree = PrintBinaryTree()
response = print_tree.print_tree(node)
print(response)
