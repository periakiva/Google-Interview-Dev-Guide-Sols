class sol:
    def ransom(self,numWordsinMagazine,numWordsInRansom,wordsMagazine,Ransom):
        if numWordsinMagazine<numWordsInRansom:
            return "No"
        maglist = [word for word in wordsMagazine.split()]
        ranlist = [word for word in Ransom.split()]
        
        print maglist
        print ranlist
        ransSum= sum(map(hash,ranlist))
        check = False
        for i in xrange(0,len(ranlist)):
            if maglist.count(ranlist[i])==ranlist.count(ranlist[i]):
                #print ranlist[i] + str(maglist.count(ranlist[i]))
                #print ranlist.count(ranlist[i])
                check = True
            else:
                return "No"
        if check:
            return "Yes"
    

mag = "two two time three is not four"
rans = "two time two is four"
numWordsInRansom = len(rans)
numWordsinMagazine = len(mag)
a = sol()
print a.ransom(numWordsinMagazine,numWordsInRansom,mag,rans)
