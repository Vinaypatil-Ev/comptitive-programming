class BST:
    class Node:
        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None
    def __init__(self):
        self.bst = None
        
    def insert_(self, root,value):
        if root == None:
            return
        if value < root.value:
            if root.left is None:
                root.left = self.Node(value)
            else:
                self.insert_(root.left, value)
        elif value > root.value:
            if root.right is None:
                root.right = self.Node(value)
            else:
                self.insert_(root.right, value)