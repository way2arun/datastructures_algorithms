"""
Convert Sorted List to Binary Search Tree
Given the head of a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.



Example 1:


Input: head = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: One possible answer is [0,-3,9,-10,null,5], which represents the shown height balanced BST.
Example 2:

Input: head = []
Output: []
Example 3:

Input: head = [0]
Output: [0]
Example 4:

Input: head = [1,3]
Output: [3,1]


Constraints:

The number of nodes in head is in the range [0, 2 * 104].
-10^5 <= Node.val <= 10^5
"""
from src.trees.printBinaryTree import PrintBinaryTree

# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        # Solution 1 - 136 ms
        """
        def helper(beg, end):
            if beg > end: return None
            mid = (beg + end) // 2
            left = helper(beg, mid - 1)
            root = TreeNode(self.head.val)
            self.head = self.head.next
            root.left = left
            root.right = helper(mid + 1, end)
            return root

        self.head, copy, n = head, head, 0
        while copy:
            copy = copy.next
            n += 1

        return helper(0, n - 1)
        """
        # Solution 2 - 92 ms
        if head is None:
            return None
        if head.next is None:
            return TreeNode(head.val)
        if head.next.next is None:
            return TreeNode(head.next.val, left=TreeNode(head.val))
        if head.next.next.next is None:
            return TreeNode(head.next.val, left=TreeNode(head.val), right=TreeNode(head.next.next.val))

        p0 = head
        p1 = head
        p2 = None

        while p0 is not None:
            p2 = p1
            if p0.next is not None:
                p0 = p0.next
            p1 = p1.next
            p0 = p0.next

        p2.next = None

        return TreeNode(p1.val, left=self.sortedListToBST(head), right=self.sortedListToBST(p1.next))


# Main Call
head = ListNode(-10)
head.next = ListNode(-3)
head.next.next = ListNode(0)
head.next.next.next = ListNode(5)
head.next.next.next.next = ListNode(9)

solution = Solution()
node = solution.sortedListToBST(head)
print(node)
print_tree = PrintBinaryTree()
response = print_tree.print_tree(node)

