class sol:
    def steps(self,n):
        a = [1,2,3]
        for i in range(0,n-2):
            a.append(a[-1]+a[-2])
        print a
        return a[-1]

a = sol()
n=3
print a.steps(n)
