class sol:
    def findPeak(self,arr):
        peaks=[]
        for i in xrange(0,len(arr)):
            if arr[i]>arr[i-1] and arr[i]>arr[i+1]:
                peaks = peaks+[arr[i]]
        return peaks

arr = [1,4,3,6,7,5]
a=sol()
print a.findPeak(arr)
