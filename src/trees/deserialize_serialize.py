"""
Serialize and Deserialize BST
Serialization is converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary search tree. There is no restriction on how your serialization/deserialization algorithm should work. You need to ensure that a binary search tree can be serialized to a string, and this string can be deserialized to the original tree structure.

The encoded string should be as compact as possible.



Example 1:

Input: root = [2,1,3]
Output: [2,1,3]
Example 2:

Input: root = []
Output: []


Constraints:

The number of nodes in the tree is in the range [0, 104].
0 <= Node.val <= 104
The input tree is guaranteed to be a binary search tree.
"""
from typing import List

from src.trees.printBinaryTree import PrintBinaryTree


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def serialize1(root: TreeNode) -> str:
    """Return a string of node values in preorder traversal"""
    data = []

    def dfs(node):
        if node:
            data.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

    dfs(root)
    return ','.join(data)


def deserialize1(data: List[str]) -> TreeNode:
    """Use preorder and inorder traversal data to recover a bst
    This approach assumes the node values of the bst are distinct

    """
    if not data:
        return None

    preorder = [int(x) for x in data.split(',')]
    inorder = sorted(preorder)

    node_to_inorder_index = {v: i for i, v in enumerate(inorder)}

    def build_binary_tree(preorder_start, preorder_end,
                          inorder_start, inorder_end):
        """Build a binary tree from
        preorder[preorder_start: preorder_end]
        inorder[inorder_start: inorder_end]
        """
        if preorder_start >= preorder_end:
            return None

        root_inorder_index = node_to_inorder_index[preorder[preorder_start]]

        # inorder traversal of the left substree
        # is inorder[inorder_start: root_inorder_index]
        left_tree_size = root_inorder_index - inorder_start

        left = build_binary_tree(preorder_start + 1, preorder_start + 1 + left_tree_size,
                                 inorder_start, root_inorder_index
                                 )

        right = build_binary_tree(preorder_start + left_tree_size + 1, preorder_end,
                                  root_inorder_index + 1, inorder_end
                                  )

        root = TreeNode(inorder[root_inorder_index])
        root.left = left;
        root.right = right

        return root

    return build_binary_tree(0, len(preorder), 0, len(inorder))

def serialize2(root):
    return root

def deserialize2(data):
    return data

class Codec:
    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        # Solution 1 - 76 ms
        """
        if not root: return ""
        stack, out = [root], []
        while stack:
            cur = stack.pop()
            out.append(cur.val)
            for child in filter(None, [cur.right, cur.left]):
                stack += [child]

        print(out)
        return ' '.join(map(str, out))
        """
        # Solution 2 - 48 ms
        return serialize2(root)


    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        # Solution 1 - 76 ms
        """
        preorder = [int(i) for i in data.split()]

        def helper(down, up):
            if self.idx >= len(preorder): return None
            if not down <= preorder[self.idx] <= up: return None
            root = TreeNode(preorder[self.idx])
            self.idx += 1
            root.left = helper(down, root.val)
            root.right = helper(root.val, up)
            return root

        self.idx = 0
        return helper(-float("inf"), float("inf"))
        """
        # Solution 2 - 48 ms
        return deserialize2(data)


# Main call
treenode = TreeNode(2)
treenode.left = TreeNode(1)
treenode.right = TreeNode(3)

serialize = Codec()
deserialize = Codec()
tree = serialize.serialize(treenode)
node = deserialize.deserialize(tree)

# Lets print the binary tree
print_tree = PrintBinaryTree()
response = print_tree.print_tree(node)
print(response)
