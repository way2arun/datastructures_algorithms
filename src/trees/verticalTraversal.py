"""
Vertical Order Traversal of a Binary Tree
Given a binary tree, return the vertical order traversal of its nodes values.

For each node at position (X, Y), its left and right children respectively will be at positions (X-1, Y-1) and (X+1, Y-1).

Running a vertical line from X = -infinity to X = +infinity, whenever the vertical line touches some nodes, we report the values of the nodes in order from top to bottom (decreasing Y coordinates).

If two nodes have the same position, then the value of the node that is reported first is the value that is smaller.

Return an list of non-empty reports in order of X coordinate.  Every report will have a list of values of nodes.



Example 1:



Input: [3,9,20,null,null,15,7]
Output: [[9],[3,15],[20],[7]]
Explanation:
Without loss of generality, we can assume the root node is at position (0, 0):
Then, the node with value 9 occurs at position (-1, -1);
The nodes with values 3 and 15 occur at positions (0, 0) and (0, -2);
The node with value 20 occurs at position (1, -1);
The node with value 7 occurs at position (2, -2).
Example 2:



Input: [1,2,3,4,5,6,7]
Output: [[4],[2],[1,5,6],[3],[7]]
Explanation:
The node with value 5 and the node with value 6 have the same position according to the given scheme.
However, in the report "[1,5,6]", the node value of 5 comes first since 5 is smaller than 6.


Note:

The tree will have between 1 and 1000 nodes.
Each node's value will be between 0 and 1000.
"""

# Definition for a binary tree node.
from collections import defaultdict, deque
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        # Solution 1 - 32 ms
        """
        result = defaultdict(list)
        self.DFS(root, 0, 0, result)

        result_sorted = sorted(result.keys(), reverse=True)
        dic = defaultdict(list)
        for cord in result_sorted:
            dic[cord[0]].extend(sorted(result[cord]))  # sorting because there may be more than one values at same position.
        output = list(dic.values())
        return output[::-1]
        """
        # Solution 2 - 16 ms
        if not root:
            return []

        cols = defaultdict(list)
        queue = deque([(root, 0, 0)])
        min_col = max_col = 0
        result = []

        while queue:
            node, row, col = queue.popleft()
            if node:
                cols[col].append((row, node.val))
                min_col = min(min_col, col)
                max_col = max(max_col, col)

                if node.left:
                    queue.append((node.left, row + 1, col - 1))

                if node.right:
                    queue.append((node.right, row + 1, col + 1))

        for col in range(min_col, max_col + 1):
            result.append([val for row, val in sorted(cols[col])])

        return result

    def DFS(self, root, x, y, result):

        if root is None:
            return
        result[(x, y)].append(root.val)  # store the values at coord(x,y)
        self.DFS(root.left, x - 1, y - 1, result)
        self.DFS(root.right, x + 1, y - 1, result)


# Main Call
tree_root = TreeNode(1)
tree_left_1 = TreeNode(2)
tree_right_1 = TreeNode(3)
tree_left_2 = TreeNode(4)
tree_left_3 = TreeNode(5)
tree_right_left_4 = TreeNode(6)
tree_right_right_5 = TreeNode(7)

tree_root.left = tree_left_1
tree_left_1.left = tree_left_2
tree_left_1.right = tree_left_3
tree_root.right = tree_right_1
tree_right_1.left = tree_right_left_4
tree_right_1.right = tree_right_right_5

solution = Solution()
print(solution.verticalTraversal(tree_root))
