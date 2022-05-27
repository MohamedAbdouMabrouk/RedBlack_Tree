from RBTreeClasses import NodeClass


class RBTree:
    def __init__(self):
        self.size = 0
        self.nil = NodeClass.Node(0)
        self.nil.red = False
        self.nil.left = None
        self.nil.right = None
        self.root = self.nil

    def insert(self, value):
        new_node = NodeClass.Node(value)
        new_node.red = True
        new_node.right = self.nil
        new_node.left = self.nil
        new_node.parent = None

        parent = None
        current = self.root
        while current != self.nil:
            parent = current
            if new_node.value < current.value:
                current = current.left
            elif new_node.value > current.value:
                current = current.right
            else:
                print("ERROR: Word already in the dictionary")
                return

        new_node.parent = parent
        if not parent:
            self.root = new_node
        elif new_node.value < parent.value:
            parent.left = new_node
        else:
            parent.right = new_node

        self.size += 1
        self.fix_insert(new_node)

    def fix_insert(self, new_node):
        while new_node != self.root and new_node.parent.red:
            if new_node.parent == new_node.parent.parent.right:
                u = new_node.parent.parent.left
                if u.red:
                    u.red = False
                    new_node.parent.red = False
                    new_node.parent.parent.red = True
                    new_node = new_node.parent.parent
                else:
                    if new_node == new_node.parent.left:
                        new_node = new_node.parent
                        self.rotate_right(new_node)
                    new_node.parent.red = False
                    new_node.parent.parent.red = True
                    self.rotate_left(new_node.parent.parent)
            else:
                u = new_node.parent.parent.right
                if u.red:
                    u.red = False
                    new_node.parent.red = False
                    new_node.parent.parent.red = True
                    new_node = new_node.parent.parent
                else:
                    if new_node == new_node.parent.right:
                        new_node = new_node.parent
                        self.rotate_left(new_node)
                    new_node.parent.red = False
                    new_node.parent.parent.red = True
                    self.rotate_right(new_node.parent.parent)
        self.root.red = False

    def rotate_right(self, node):
        y = node.left
        node.left = y.right
        if y.right != self.nil:
            y.right.parent = node
            
        y.parent = node.parent
        if not node.parent:
            self.root = y
        elif node == node.parent.right:
            node.parent.right = y
        else:
            node.parent.left = y
        y.right = node
        node.parent = y

    def rotate_left(self, node):
        y = node.right
        node.right = y.left
        if y.left != self.nil:
            y.left.parent = node

        y.parent = node.parent
        if not node.parent:
            self.root = y
        elif node == node.parent.left:
            node.parent.left = y
        else:
            node.parent.right = y
        y.left = node
        node.parent = y

    def search(self, value):
        current = self.root
        while value != current.value and current != self.nil:
            if value > current.value:
                current = current.right
            else:
                current = current.left
        return current

    def height(self, root):
        if root == self.nil:
            return 0
        left_side = self.height(root.left)
        right_side = self.height(root.right)
        return max(left_side, right_side) + 1
