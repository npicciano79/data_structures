#binary trees

#tree constructor
class Tree:
    def __init__(self, data,left=None,right=None):
        self.data=data
        self.left=left
        self.right=right
    def create(self,data):
        if self.data==data:      #entered dupilcate value
            return False
        elif self.data>data:
            if self.left is not None:
                return self.left.create(data)
            else:
                self.left=Tree(data)
                return True
        else:
            if self.right is not None:
                return self.right.create(data)
            else:
                self.right=Tree(data)
                return True
    def find(self, data):
        if self.data==data:
            return data
        elif self.data>data:
            if self.left is None:
                return False
            else:
                return self.left.find(data)
        elif self.data<data:
            if self.right is None:
                return False
            else:
                return self.right.find(data)
    #inorder traversal
    def inorder(self):
        if self is not None:
            if self.left is not None:
                self.left.inorder()
        print(self.data,end=' /')
        if self.right is not None:
            self.right.inorder()
    
    #preorder traversal
    def preorder(self):
        if self is not None:
            print(self.data,end='-')
            if self.left is not None:
                self.left.preorder()
            if self.right:
                self.right.preorder()

    def postorder(self):
        if self is not None:
            if self.left is not None:
                self.left.postorder()
            if self.right is not None:
                self.right.postorder()
            print(self.data,end=' ')



    #get tree size
    def get_size(self):
        if self.left is not None and self.right is not None:
            return 1+self.left.get_size()+self.right.get_size()
        elif self.left:
            return 1+self.left.get_size()
        elif self.right:
            return 1 + self.right.get_size()
        else:
            return 1




vals=[15,10,2,12,3,1,13,6,11,4,14,9]
tree=Tree(7)
tree.create(9)
for i in vals:
    tree.create(i)
#print(tree.find(12))
#tree.inorder()
#tree.preorder()
tree.postorder()
#print(tree.get_size())



# C:/Users/npicc/Documents/python/python.exe c:/Users/npicc/Documents/Coding/projects/data_structures/binary_trees.py