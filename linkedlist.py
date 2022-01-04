#linked list code
class Node:
    def __init__(self,data,n=None,p=None):
        self.data=data
        self.next=n
        self.prev=p

    def __str__(self):
        return('('+str(self.data)+')')

class LinkedList:
    def __init__(self,r=None):
        self.root=r
        self.size=0
    
    def add(self,d):
        new_node=Node(d,self.root)
        self.root=new_node
        self.size+=1
    def find(self,d):
        this_node=self.root
        while this_node is not None:
            if this_node.data==d:
                return d
            else:
                this_node=this_node.next_node
            return None

linkedlist=LinkedList()
linkedlist.add(3)
linkedlist.add(4)
linkedlist.add(10)
