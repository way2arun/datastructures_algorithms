"""
Verify Preorder Serialization of a Binary Tree
One way to serialize a binary tree is to use preorder traversal. When we encounter a non-null node, we record the node's value. If it is a null node, we record using a sentinel value such as '#'.


For example, the above binary tree can be serialized to the string "9,3,4,#,#,1,#,#,2,#,6,#,#", where '#' represents a null node.

Given a string of comma-separated values preorder, return true if it is a correct preorder traversal serialization of a binary tree.

It is guaranteed that each comma-separated value in the string must be either an integer or a character '#' representing null pointer.

You may assume that the input format is always valid.

For example, it could never contain two consecutive commas, such as "1,,3".
Note: You are not allowed to reconstruct the tree.



Example 1:

Input: preorder = "9,3,4,#,#,1,#,#,2,#,6,#,#"
Output: true
Example 2:

Input: preorder = "1,#"
Output: false
Example 3:

Input: preorder = "9,#,#,1"
Output: false


Constraints:

1 <= preorder.length <= 104
preoder consist of integers in the range [0, 100] and '#' separated by commas ','.
"""


class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        # Solution 1 - 20 ms
        """
        nodes = preorder.split(',')
        slots = 1
        for node in nodes:
            if slots <= 0: return False
            slots += -1 if node == '#' else 1
        return slots == 0
        """
        # Solution 2 - 16 ms
        """
                One way to serialize a binary tree is to use preorder traversal. 
                When we encounter a non-null node, we record the node's value. 
                If it is a null node, we record using a sentinel value such as '#'.
                Given a string of comma-separated values preorder, 
                return true if it is a correct preorder traversal serialization of a binary tree.
                Use stack to store visited nodes.
                If arriving at leaf nodes or both left and right subtree has visited (marked as '#'),
                replace the top stack node as '#' and continue pre-order visits.
                If stack is empty on the way, return False.
                At the last, check whether stack only has one '#' left (root).
                Time complexity: O(N)
                Space complexity: O(N)
                """
        # base case
        if not preorder:
            return True
        # use stack to store visited nodes
        stack = []
        for node in preorder.split(','):
            while node == '#' and stack and stack[-1] == '#':
                stack.pop()
                if not stack:
                    return False
                stack.pop()
            stack.append(node)
        return stack == ['#']

# Main Call
preorder = "9,3,4,#,#,1,#,#,2,#,6,#,#"
solution = Solution()
print(solution.isValidSerialization(preorder))