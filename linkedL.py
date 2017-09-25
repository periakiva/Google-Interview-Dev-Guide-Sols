class Node:
    def __init__(self,data,index):
        self.data=data
        self.next=None
        self.index=index
    
    def _insertNode(self,data):
        temp = self
        while temp.next != None:
            temp=temp.next
        temp.next=Node(data,temp.index+1)

    def _printList(self):
        temp = self
        while temp != None:
            print [temp.data,temp.index],
            temp=temp.next

    def _delNode(self,index):
        prev=None
        temp=self
        if index==0:
            self=self.next
            return self 
        else:
            while temp!=None and temp.index!=index:
                prev=temp
                temp=temp.next
            if temp==None:
                print "index not found, list stays the same"
                return self
            elif temp.index==index:
                prev.next=temp.next
                return self




class List:
    def __init__(self):
        self.head=None
    
    def delNode(self,index):
        if not self.head:
            print "No LL"
            return False
        else:
            self.head=self.head._delNode(index)

    def insertNode(self,data):
        if self.head==None:
            self.head = Node(data,0)
            return True
        else:
            self.head._insertNode(data)

    def printList(self):
        if self.head == None:
            print "No list"
            return False
        else:
            self.head._printList()




if __name__ == '__main__':
    ll = List()
    ll.insertNode(2)
    ll.insertNode(3)
    ll.insertNode(4)
    ll.insertNode(5)
    ll.insertNode(6)
    ll.printList()
    print "\n"
    ll.delNode(4)
    ll.printList()
