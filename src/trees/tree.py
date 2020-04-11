"""
Tree implementation
"""


class TreeNode:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None


class Tree:
    def createNode(self, data):
        """

        :param data:
        :return:
        """
        return TreeNode(data)

    def insert(self, node, data):
        """

        :param node:
        :param data:
        :return:
        """
        # if tree is empty , return a root node
        if node is None:
            return self.createNode(data)

        # if data is smaller than parent , insert it into left side
        if data < node.data:
            node.left = self.insert(node.left, data)
        elif data > node.data:
            node.right = self.insert(node.right, data)

        return node

    def search(self, node, data):
        """

        :param node:
        :param data:
        :return:
        """
        # if root is None or root is the search data.
        if node is None or node.data == data:
            return node

        if node.data < data:
            return self.search(node.right, data)
        else:
            return self.search(node.left, data)

    def deleteNode(self, node, data):
        """

        :param node:
        :param data:
        :return:
        """
        # Check if tree is empty.
        if node is None:
            return None

        # searching key into BST.
        if data < node.data:
            node.left = self.deleteNode(node.left, data)
        elif data > node.data:
            node.right = self.deleteNode(node.right, data)
        else:  # reach to the node that need to delete from BST.
            if node.left is None and node.right is None:
                del node
            if node.left == None:
                temp = node.right
                del node
                return temp
            elif node.right == None:
                temp = node.left
                del node
                return temp

        return node

    def inorder(self, root):
        """

        :param root:
        :return:
        """
        if root is not None:
            self.inorder(root.left)
            print(root.data)
            self.inorder(root.right)

    def preorder(self, root):
        """

        :param root:
        :return:
        """
        if root is not None:
            print(root.data)
            self.preorder(root.left)
            self.preorder(root.right)

    def postorder(self, root):
        """

        :param root:
        :return:
        """
        if root is not None:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data)


def main():
    root = None
    tree = Tree()
    root = tree.insert(root, 10)
    tree.insert(root, 20)
    tree.insert(root, 30)
    tree.insert(root, 40)
    tree.insert(root, 70)
    tree.insert(root, 60)
    tree.insert(root, 80)

    print("In-order traversing")
    tree.inorder(root)

    print("Pre-order traversing")
    tree.preorder(root)

    print("Post-order traversing")
    tree.postorder(root)


if __name__ == "__main__":
    main()
