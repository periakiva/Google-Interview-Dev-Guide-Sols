import math
def findPow(n):
    factor=2
    ntemp=n
    for base in xrange(0,int(math.sqrt(n))):
        for factor in xrange(2,n):
            print "base^factor: " + str(math.pow(base,factor))
            if math.pow(base,factor)==n:
                return True
            if math.pow(base,factor)>n:
                continue
    return False
print findPow(120)

