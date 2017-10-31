def sol(a,b):
    counter =1
    for i in xrange(0,len(b)):
        if a.find(b[i])==-1:
            return -1
    while a.find(b)!=2:
        counter+=1
        a=counter*a
        print a
    return counter

a = "abcd"
b="cdabcdabz"
print sol(a,b)
