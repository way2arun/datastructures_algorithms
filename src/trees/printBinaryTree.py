from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class PrintBinaryTree:
    def print_tree(self, root: TreeNode) -> List[List[str]]:
        # Get the height of the tree
        self.height = self.get_height(root)
        print(self.height)
        d = 2 ** self.height - 1
        # build the matrix
        result = [["" for i in range(d)] for j in range(self.height)]
        # draw on the matrix
        self.draw(root, result, self.height, d // 2)
        return result

    def draw(self, node, result, height, position):
        # draw the node
        result[self.height - height][position] = str(node.val)

        # if this is the lowest level, we are done
        if height == 1:
            return

        # calculate the depth of the current node
        node_depth = self.height - height + 1

        # how much away should we place the child node(s)
        child_sep = 2 ** (self.height - node_depth - 1)

        # recursively draw the children node (DFS)
        if node.left is not None:
            child_pos = position - child_sep
            self.draw(node.left, result, height - 1, child_pos)
        if node.right is not None:
            child_pos = position + child_sep
            self.draw(node.right, result, height - 1, child_pos)

    def get_height(self, node):
        if node.left is None and node.right is None:
            return 1

        if node.left is None and node.right is not None:
            return 1 + self.get_height(node.right)

        if node.left is not None and node.right is None:
            return 1 + self.get_height(node.left)

        if node.left is not None and node.right is not None:
            return 1 + max(self.get_height(node.left), self.get_height(node.right))
