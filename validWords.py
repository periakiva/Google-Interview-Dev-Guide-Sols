class sol:
    def __init__(self):
        self.words = ["hello","learn","learning","linked","list","platform","programming","stack","heaps"]

    def valid(self,s):
        result=[]
        if s in self.words:
            result.append([s])
        result+=[[s[:i]] + word for i in range(1,len(s)) for word in self.valid(s[i:]) if s[:i] in self.words] 
        return result
a = sol()
s = "hellolearninglearnlinkedplatform"
print a.valid(s)
