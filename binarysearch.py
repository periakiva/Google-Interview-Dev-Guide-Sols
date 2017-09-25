

def bSearch(arr,low,high,value):
    middle = (high+low)/2
    print "current arr: " + str(arr)
    #print middle
    if not arr:
        return
    if arr[middle]==value:
        print "found"
        print middle
        return value

    print "arr middle: " + str(arr[middle])
    if arr[middle]<value:
        index = bSearch(arr,middle,high,value)
        if index:
            return index
    elif arr[middle]>value:
        index = bSearch(arr,0,middle,value)
        if index:
            return index

    

arr=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
bSearch(arr,0,len(arr),8)
