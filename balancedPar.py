def balPar(string):
    dic = {'(':')'}
    so =[]
    for i in range(0,len(string)):
        print "string[i]: " + str(string[i])
        if so:
            print "so[-1]: " + str(so[-1])
        if (string[i] in dic.values()) or (string[i] in dic):
            so+=[string[i]]
        if len(so)>1:
            if so and string[i]==so[-2]:
                print "popping"
                so.pop()
                so.pop()
                print so
    return so

def countPar(string):
    count=0
    for i in range(0,len(string)):
        if string[i]=='(':
            count+=1
        elif string[i]==')':
            if count==0:
                return False
            else:
                count-=1
    return count

s = "((BCD)AE)"
print countPar(s)

