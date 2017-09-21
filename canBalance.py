class sol:
    def canBalance(self,arr):
        print sum(arr)%2
        if sum(arr)%2==0:
            return True
        else:
            return False

a = sol()
arr = [1,5,421,3,2,1,4,65,3,1,1,2,1]
print a.canBalance(arr)
