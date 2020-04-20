from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class PrintBinaryTree:
    def printTree(self, root: TreeNode) -> List[List[str]]:
        # find depth of the tree
        self.depth = self.get_height(root)
        d = 2 ** self.depth - 1
        # build the matrix
        result = [["" for i in range(d)] for j in range(self.depth)]
        # draw on the matrix
        self.draw(root, result, self.depth, d // 2)
        return result

    def draw(self, node, res, height, pos):
        # draw the node
        res[self.depth - height][pos] = str(node.val)

        # if this is the lowest level, we are done
        if height == 1:
            return

        # calculate the depth of the current node
        node_depth = self.depth - height + 1

        # how much away should we place the child node(s)
        child_sep = 2 ** (self.depth - node_depth - 1)  # self.depth is the depth of the whole tree

        # recursively draw the children node (DFS)
        if node.left is not None:
            child_pos = pos - child_sep
            self.draw(node.left, res, height - 1, child_pos)
        if node.right is not None:
            child_pos = pos + child_sep
            self.draw(node.right, res, height - 1, child_pos)

    def get_height(self, node):
        if node.left is None and node.right is None:
            return 1

        if node.left is None and node.right is not None:
            return 1 + self.get_height(node.right)

        if node.left is not None and node.right is None:
            return 1 + self.get_height(node.left)

        if node.left is not None and node.right is not None:
            return 1 + max(self.get_height(node.left), self.get_height(node.right))
