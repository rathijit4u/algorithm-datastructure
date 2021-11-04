import timerutil
import logger


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, value):

        if value <= self.data:
            if self.left is None:
                self.left = Node(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = Node(value)
            else:
                self.right.insert(value)

    def print_tree(self):
        if self.data is None:
            return
        else:
            if self.left is not None:
                self.left.print_tree()

            logger.info(self.data)

            if self.right is not None:
                self.right.print_tree()

    def contains(self, key):
        if self.data == key:
            return True
        elif key < self.data:
            if self.left is not None:
                return self.left.contains(key)
            else:
                return False
        else:
            if self.right is not None:
                return self.right.contains(key)
            else:
                return False


if __name__ == "__main__":
    input_tree = [1, 0, 1, 0, 1, 0, 1]
    root_node = Node(input_tree[0])
    for x in input_tree[1:]:
        root_node.insert(x)
    root_node.print_tree()
    bst_node = Node(20)
    bst_node.insert(10)
    bst_node.insert(30)
    bst_node.print_tree()
    logger.info(bst_node.contains(40))
    logger.info(bst_node.contains(30))
