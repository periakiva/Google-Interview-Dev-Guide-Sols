
from random import randint

class Node:
    def __init__(self,data=None,left=None,right=None):
        self.data=data
        self.left = left
        self.right = right
    
    def _insert(self,data):
        if data==self.data:
            return False
        elif data<self.data:
            if self.left:
                self.left._insert(data)
            else:
                self.left=Node(data)
        elif data>self.data:
            if self.right:
                self.right._insert(data)
            else:
                self.right = Node(data)

    def _inorder(self):
        if self.left:
            self.left._inorder()
        print(self.data)
        if self.right:
            self.right._inorder()

    def _search(self,data):
        if self.data==data:
            print "Found"
            return True
        elif self.data>data and self.left:
            print "going left"
            self.left._search(data)
        elif self.data<data and self.right:
            print "going right"
            self.right._search(data)
    
    def _print_indented(self,level=0):
        #print not self
        if not self.data: return
        if self.left:
            self.left._print_indented(level+1)
        print '  '*level + str(self.data)
        if self.right:
            self.right._print_indented(level+1)
    
    def _del(self,data):
        parent = None
        node = self
        while node and node.data != data:
            parent = node
            if data<node.data:
                node = parent.left
            elif data > node.data:
                node = parent.right
        if node is None or node.data!=data:
            return False

        elif (node.left == None) and (node.right == None):
            if data<parent.data:
                parent.left = None
            else:
                parent.right = None
            return True
        
        elif node.left and (node.right == None):
            print "node.left and node.right is None"
            if data < parent.data:
                parent.left = node.left
                return True
            else:
                parent.right = node.left
                return True

        elif node.right and (node.left == None):
            print "node.right and node.left not is None"
            if data < parent.data:
                parent.left = node.right
                return True
            else:
                parent.right = node.right
                return True

        elif node.right and node.left:
            print "hello"
            tempNode=node.right
            tempPnode = node
            while tempNode.left is not None:
                tempNode = tempNode.left
            print tempNode.data
            node.data=tempNode.data
            tempNode._del(data)
        return self
    def _isBST(self):
        if self.left==None and self.right==None:
            return          
        if self.right and self.left:
            if self.right.data>self.left.data and self.right.data>self.data and self.left.data<self.data:
                print "so far so good"
            else:
                print "nope"
                return False
        elif self.right and self.left == None:
            if self.right.data>self.data:
                print "so far so good"
            else:
                print "nope"
                return False
        elif self.left and self.right==None:
            if self.left.data<self.data:
                print "so far so good"
            else:
                print "nope"
                return False
        if self.left:
            self.left._isBST()
        if self.right:
            self.right._isBST()
        return True

class Tree:
    def __init__(self):
        self.root = None

    def isBST(self):
        if self:
            print "going in"
            return self.root._isBST()
        else:
            return False

    def longestPath(self):
        if self.root:
            self.root._longestPath()
        else:
            print "No root"

    def insert(self,data):
        if self.root:
            return self.root._insert(data)
        else:
            self.root = Node(data)
            return True

    def dele(self,data):
        if self.root:
            print "start remove"
            return self.root._del(data)
        else:
            print "No data in tree, nothing to delete"

    def inorder(self):
        if self.root:
            self.root._inorder()
        else:
            print "Tree is empty"
    
    def print_indented(self):
        if not self.root:
            return
        else:
            self.root._print_indented()

    def search(self,data):
        if self.root:
            self.root._search(data)
        else:
            print "There is not tree"
            return False

list = [1,2,3,4,5,6,7]
tree = Tree()
#tree.insertList(list)
#for i in xrange(0,10):
#    tree.insert(randint(0,10))
tree.insert(4)
tree.insert(6)
tree.insert(3)
tree.insert(1)
tree.insert(5)
tree.insert(15)
tree.insert(10)
tree.insert(11)
tree.insert(9)
tree.insert(2)
#tree.search(7)
tree.inorder()
#tree.print_indented()
print tree.dele(6)
#tree.print_indented()
tree.inorder()
print tree.isBST()
