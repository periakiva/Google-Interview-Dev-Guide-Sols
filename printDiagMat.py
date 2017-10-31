def matPr(mat):
    size = 0
    m = len(mat)-1
    n=len(mat[0])-1
    print m
    print n
    sub={}
    for i in xrange(0,n+1):
        for j in xrange(0,m+1):
            if (i+j) not in sub:
                sub[i+j]=[mat[j][i]]
            else:
                sub[i+j]=sub[i+j]+[mat[j][i]]
    for i in sub:
        print sub[i]
    return sub




arr = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20]]
print arr[1][1]
print matPr(arr)
