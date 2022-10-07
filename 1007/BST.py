# Has in-order, pre-order, post-order print
class BST:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right  
    def insert(self, key):
        if self.key == key:
            return
        elif self.key < key:
            if self.right is None:
                self.right = BST(key)
            else:
                self.right.insert(key)
        else: 
            if self.left is None:
                self.left = BST(key)
            else:
                self.left.insert(key)

    def inorder(self):
        if self.left:
            self.left.inorder()
        print(self.key, end= " ")
        if self.right:
            self.right.inorder()

    def preorder(self):
        print(self.key, end = " ")
        if self.left:
            self.left.preorder()
        if self.right: 
            self.right.preorder()

    def postorder(self):
        if self.left:
            self.left.preorder()
        if self.right: 
            self.right.preorder()
        print(self.key, end = " ")

myBST = BST(3, BST(1), BST(5))

myBST.inorder()
print()
myBST.preorder()
print()
myBST.postorder()
