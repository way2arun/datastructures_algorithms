"""
 Populating Next Right Pointers in Each Node
You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:

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



Input: root = [1,2,3,4,5,6,7]
Output: [1,#,2,3,#,4,5,6,7,#]
Explanation: Given the above perfect binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.


Constraints:

The number of nodes in the given tree is less than 4096.
-1000 <= node.val <= 1000
"""

# Definition for a binary tree node.
from src.trees.printBinaryTree import PrintBinaryTree


# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        # Solution 1 - 56 ms
        """
        if not root or not root.left:
            return root

        self.connect(root.left)
        self.connect(root.right)

        lft = root.left
        rgh = root.right
        lft.next = rgh

        while lft.right:
            lft = lft.right
            rgh = rgh.left
            lft.next = rgh

        return root
        """
        # Solution 2 - 40 ms
        ret = root  # save variable to return

        while root and root.left:  # while we are not at the end of the tree
            next = root.left  # the next node is the left node
            while root:  # while we are not at the end
                root.left.next = root.right  # the left root will point to the right root
                if root.next:  # if there is a root still
                    root.right.next = root.next.left  # the next one of the right one is the next one of the left
                else:
                    root.right.next = None  # otherwise we are at the rightmost roots so set to None
                root = root.next  # go to the next root
            root = next

        return ret



# Main Call
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

solution = Solution()
node = solution.connect(root)
# Lets print the binary tree
print_tree = PrintBinaryTree()
response = print_tree.print_tree(node)
print(response)
