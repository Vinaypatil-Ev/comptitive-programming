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
            
    def insert(self, value):
        self.insert_(self, self.root, value)
        
    def delete_(self, root, value):
        if root is None:
            return
        if value < root.value:
            root.left = self.delete_(root.left, value)
        elif value > root.value:
            root.right = self.delete_(root.right, value)
        else:
            if root.left is None and root.right is None:
                del(root)
                return 
            elif root.left is None:
                temp = root.right
                del(root)
                return temp
            elif root.right is None:
                temp = root.right
                del(root)
                return temp
        return root
            
    
    def delete(self, value):
        pass