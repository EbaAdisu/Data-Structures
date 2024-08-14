class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = TreeNode(value)
        else:
            self._insert(self.root, value)

    def _insert(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = TreeNode(value)
            else:
                self._insert(node.left, value)
        else:
            if node.right is None:
                node.right = TreeNode(value)
            else:
                self._insert(node.right, value)

    def search(self, value):
        return self._search(self.root, value)

    def _search(self, node, value):
        if node is None or node.value == value:
            return node
        if value < node.value:
            return self._search(node.left, value)
        return self._search(node.right, value)

    def in_order_traversal(self):
        return self._in_order_traversal(self.root, [])

    def _in_order_traversal(self, node, traversal):
        if node is not None:
            self._in_order_traversal(node.left, traversal)
            traversal.append(node.value)
            self._in_order_traversal(node.right, traversal)
        return traversal

    def pre_order_traversal(self):
        return self._pre_order_traversal(self.root, [])

    def _pre_order_traversal(self, node, traversal):
        if node is not None:
            traversal.append(node.value)
            self._pre_order_traversal(node.left, traversal)
            self._pre_order_traversal(node.right, traversal)
        return traversal

    def post_order_traversal(self):
        return self._post_order_traversal(self.root, [])

    def _post_order_traversal(self, node, traversal):
        if node is not None:
            self._post_order_traversal(node.left, traversal)
            self._post_order_traversal(node.right, traversal)
            traversal.append(node.value)
        return traversal

    def find_min(self):
        return self._find_min(self.root)

    def _find_min(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current.value

    def find_max(self):
        return self._find_max(self.root)

    def _find_max(self, node):
        current = node
        while current.right is not None:
            current = current.right
        return current.value

    def delete(self, value):
        self.root = self._delete(self.root, value)

    def _delete(self, node, value):
        if node is None:
            return node

        if value < node.value:
            node.left = self._delete(node.left, value)
        elif value > node.value:
            node.right = self._delete(node.right, value)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            temp = self._find_min(node.right)
            node.value = temp
            node.right = self._delete(node.right, temp)

        return node
