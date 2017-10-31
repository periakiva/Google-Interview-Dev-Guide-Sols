class sol:
    def com(self,string, step=0):
        if len(string)==1:
            return string
        perms=[]
        for c in string:
            for perm in self.com(string.replace(c,'',1)):
                perms.append(c+perm)
        return set(perms)

a = sol()
s = "stock"
print a.com(s)
