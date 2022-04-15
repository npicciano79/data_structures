#linked list code
from unittest.mock import sentinel


class Node:
   
    def __init__(self,data,n=None,p=None):
        self.data=data
        self.next=n
        self.prev=p
   
    def __str__(self):
        return('('+str(self.data)+')')
    
class LinkedList:
    def __init__(self,r=None):
        self.head=r
        self.size=0
    
    def add(self,d):
        new_node=Node(d,self.head)
        self.head=new_node
        self.size+=1


    def find(self,d):
        this_node=self.head
        while this_node is not None:
            if this_node.data==d:
                return d
            else:
                this_node=this_node.next
            return None


    def printlist(self):
        this_node=self.head
        while this_node is not None:
            print(this_node,end=" ")
            this_node=this_node.next
        print("none")

    def printlast(self):
        this_node=self.head
        if this_node==None or this_node.next==None:
            return this_node
        else:
            while this_node!=None:
                if this_node.next==None:
                    print(this_node)
                    this_node=None
                else:
                    this_node=this_node.next

    def reverseList(self,head):
        
        if head==None or head.next==None:
            return head
        p=self.reverseList(head.next)
        head.next.next=head
        head.next=None
        return p

    def removeElements(self,head,val):
        sentinel=Node(0)
        sentinel.next=self.head

        prev,curr=sentinel,self.head
        while curr:
            if curr.data==val:
                prev.next=curr.next
            else:
                prev=prev.next
            curr=curr.next
        
        return sentinel.next
       






linkedlist=LinkedList()
linkedlist.add(3)
linkedlist.add(4)
linkedlist.add(10)
linkedlist.add(12)
linkedlist.add(22)
#linkedlist.printlist()
#linkedlist.printlast()
#print(linkedlist.reverseList(22)

linkedlist.removeElements(22,12)
linkedlist.printlist()
#C:/Users/npicc/Documents/python/python.exe c:/Users/npicc/Documents/Coding/projects/data_structures/linkedlist.py
