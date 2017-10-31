def rightTr():
    n=9
    for i in range(1,n):
        print "*"*int(i),
        print " "*int(n-i)
        return
def eqTr():
    rows=10
    spaces=rows-1
    astriks=1
    for j in range(0,rows):
        for i in range(0,spaces/2):
            print " ",
        for i in range(0,astriks):
            print "*",
        astriks+=1
        for i in range((spaces/2)+astriks,rows):
            print " ",
        spaces-=1
        print "\n"
eqTr()


