class sol:
    def topProd(self,arr):
        maxprod=0
        for i in xrange(0,len(arr)-2):
            print i 
            print "arr[i] :" + str(arr[i])
            print "arr[i+1] :" + str(arr[i+1])
            print "arr[i+2] :" + str(arr[i+2])
            if arr[i]*arr[i+1]*arr[i+2]>maxprod and arr[i]<arr[i+1] and arr[i+1]<arr[i+2]:
                print "hello"
                maxprod = arr[i]*arr[i+1]*arr[i+2]
        return maxprod

a = sol()
arr=[1,23,32,4,5,6,7,8]
print arr
print a.topProd(arr)

