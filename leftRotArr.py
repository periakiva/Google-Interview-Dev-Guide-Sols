class sol:
    def leftRotation(self,arr,rots):
        ar=[]
        for i in xrange(0,len(arr)):
            ar.insert(len(ar),arr[(i+rots)%len(arr)])
        return ar
a = sol()
arr=[1,2,3,4,5]
print a.leftRotation(arr,5)



