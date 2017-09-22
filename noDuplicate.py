class sol:
    def noDup(self,arr):
        i=0
        while i < len(arr):
            print i
            print arr[i]
            if arr.count(arr[i]) > 1:
                arr.pop(i)
                i=i-1
            i=i+1
        return arr


a = sol()
arr = [1,2,3,4,3,3,3,2,1,4,5,4,3,2,5,54,3,2]
print a.noDup(arr)
