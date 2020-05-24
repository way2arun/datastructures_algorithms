"""
Return the root node of a binary search tree that matches the given preorder traversal.

(Recall that a binary search tree is a binary tree where for every node, any descendant of node.left has a value < node.val, and any descendant of node.right has a value > node.val.  Also recall that a preorder traversal displays the value of the node first, then traverses node.left, then traverses node.right.)



Example 1:

Input: [8,5,1,7,10,12]
Output: [8,5,10,1,7,null,12]



Note:

1 <= preorder.length <= 100
The values of preorder are distinct.
Reference
https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/530/week-3/3305/

"""
from typing import List
from src.trees.printBinaryTree import PrintBinaryTree


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        # 36 ms
        """
        if len(preorder) == 0:
            return None
        tree_root = TreeNode(preorder[0])
        i = 1
        while i < len(preorder) and preorder[i] < tree_root.val:
            i += 1
        tree_root.left = self.bstFromPreorder(preorder[1:i])
        tree_root.right = self.bstFromPreorder(preorder[i:])
        return tree_root
        """
        # 20 ms
        """
        self.ln = len(preorder)
        self.root = None
        self.preorder = preorder
        self.index = 0

        def traverse(min_, max_):
            if self.index >= self.ln:
                return None
            temp = None
            #print("val",self.preorder[self.index],"min_",min_,"max_",max_)
            if min_ <= self.preorder[self.index] <= max_:
                print("index",self.index)
                temp = TreeNode(self.preorder[self.index])
                self.index += 1
                temp.left = traverse(min_, temp.val)
                temp.right = traverse(temp.val, max_)
            return temp
        return traverse(-1 * float('inf'), float('inf'))
        """
        # Solution 3 16 ms
        return self.traverse(preorder, 0, len(preorder) - 1, len(preorder))

    def traverse(self, preorder: List[int], l: int, h: int, n: int) -> TreeNode:
        if n == 0 or l > h or l >= n or h >= n:
            return None
        root = TreeNode(preorder[l])
        if l == h:
            return root
        x = float('-inf')
        for i in range(l + 1, h + 1):
            if preorder[i] > root.val:
                x = i - 1
                break
        if x == float('-inf'):
            root.left = self.traverse(preorder, l + 1, h, n)
        else:
            root.left = self.traverse(preorder, l + 1, x, n)
            root.right = self.traverse(preorder, x + 1, h, n)
        return root


# Main Call
solution = Solution()
input_list = [8, 5, 1, 7, 10, 12]
print(f'Preorder :- {input_list}')
inorder = sorted(input_list)
print(f'Inorder  :- {inorder}')
result = solution.bstFromPreorder(input_list)

# Lets print the binary tree
print_tree = PrintBinaryTree()
response = print_tree.print_tree(result)
print(response)
