def path(a,e): 
    label = max(a,key=a.count)
    occ = a.count(label)
    #print occ
    l=[]
    
    graphlabels={}
    graph={}
    for i in xrange(1,len(a)+1):
        graph[i]=[]
    print graph
    
    for i in xrange(0,len(e)-1):
        graph[e[i]]=graph[e[i]]+[e[i+1]]
    print graph
    
def find_paths(graph,start,end,path):
    path = path+[start]
    if start==end:
        return [path]
    if start not in graph:
        return None
    paths=[]
    for node in graph[start]:
        if node not in path:
            newpath = find_paths(graph,node,end,path)
            for np in newpath:
                paths.append(np)
    return paths


a=[1,1,1,2,2]
e=[1,2,1,3,2,4,2,5]
path(a,e)
