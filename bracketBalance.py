class sol:
    def detectBalance(self,string):
        hash = {'{':'}','[':']','(':')'}
        sk =[]
        if len(string)%2 is not 0:
            return "NO"
        for c in string:
            if c in hash:
                sk.append(hash[c])
            elif sk and c == sk[-1]:
                sk.pop()
            else: return False
        return not sk

a = sol()
s = "{[()]}"
print a.detectBalance(s)
