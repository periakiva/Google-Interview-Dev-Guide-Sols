class sol:
    def seeSay(self,string):
        counter=1
        newstr=""
        for i in xrange(1,len(string)):
            if string[i]==string[i-1]:
                counter+=1
            else:
                newstr+=str(counter)
                newstr+=str(string[i-1])
                counter=1
            if i==len(string)-1:
                newstr+=str(counter)
                newstr+=str(string[i])
        return newstr

a = sol()
string = "aaaaagggggdddddbbbbbllrrrr"
print string
print a.seeSay(string)
