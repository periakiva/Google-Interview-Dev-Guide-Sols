class sol:
    def bigstSub(self,arr):
        arr = sorted(arr)
        sub=[]
        al=[]
        print arr
        for i in xrange(0,len(arr)-1):
            if arr[i]+1==arr[i+1]:
                sub+=[arr[i]]
                #sub+=[arr[i+1]]
                print "arr[i]: " + str(arr[i])
            if arr[i]>arr[i-1]+1:
                print "sub: " + str(sub)
                #al+=[sub]
                sub=[]
                sub+=[arr[i]]
        return al

arr = [10,12,11,32,33,34,36,37,38,56,234,2,3,4,5,6]
a = sol()
print a.bigstSub(arr)


