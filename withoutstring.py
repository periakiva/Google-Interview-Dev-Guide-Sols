
class sol:
    def withoutString(self,string,todel):
        size = len(todel)
        try:
            for i in range(0,len(string)):
                if todel == string[i:i+size]:
                    string = string.replace(string[i:i+size],"")
                    print string
        except IndexError:
            return None


a = sol()
string = "hello there"
todel = "e"
a.withoutString(string,todel)

