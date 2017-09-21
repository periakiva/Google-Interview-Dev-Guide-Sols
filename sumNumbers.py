class Solution:
    
    def sumNumbers(self,string):
        c =[]
        sum=0
        for s in xrange(0,len(string)):
            #print string[s] 
            if not string[s].isdigit():
                string = string.replace(string[s]," ")
                #print string
        for s in string.split():
            if s.isdigit():
                sum=sum+int(s)
                #c.insert(len(c),int(s))
                #print sum
        return sum

a = Solution()
string = "hello122dsfsd32sd12dsfv 322 aasdf392"
print a.sumNumbers(string)

