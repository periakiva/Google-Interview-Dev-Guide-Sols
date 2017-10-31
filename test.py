def solution(S,K):
    s=S.replace('-',"").upper()

    k=0
    for i in xrange(len(s),0,-1):
        if k==K:
            s=s[:i]+'-'+s[i:]
            k=0
        k+=1
        
    return s

print solution("2-40r7-4k",2)
