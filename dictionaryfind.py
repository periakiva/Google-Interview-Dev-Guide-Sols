
S="abppplee"
D = ["able", "ale", "apple","bale","kangaroo","shlomo","dfgjnvbnkttr","asdfbnkjhbncvnbkadsfsdg"]

def findLongString(S,D):
    D.sort(key=len,reverse=True)
    for word in D:
        checker=True
        for i in xrange(0,len(word)):
            if word[i] not in S:
                checker = False
        if not checker:
            continue
        else:
            return word

print findLongString(S,D)
