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




vals=[15,10,2,12,3,1,13,6,11,4,14,9]
tree=Tree(7)
tree.create(9)
for i in vals:
    tree.create(i)
print(tree.find(12))



# C:/Users/npicc/Documents/python/python.exe c:/Users/npicc/Documents/Coding/projects/data_structures/binary_trees.py