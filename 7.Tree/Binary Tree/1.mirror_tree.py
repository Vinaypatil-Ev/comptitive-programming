class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    

def mirror_tree(root):
    if root == None:
        return root
    temp = root.left 
    root.left = mirror_tree(root.right)
    root.right = mirror_tree(temp)
    return root

def print_tree(root):
    if root:
        print_tree(root.left)
        print(root.value, end=" ")
        print_tree(root.right)
        
        
if __name__ == "__main__":
    root = Node(5)
    root.left = Node(3)
    root.right = Node(6)
    root.left.left = Node(2)
    root.left.right = Node(4)
    print_tree(root)
    mirror_tree(root)
    print("\nmirror tree\n")
    print_tree(root)