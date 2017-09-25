
def find_shortest(graph,start,end,path):
    path = path + [start]
    if start == end:
        return path
    if start not in graph:
        return None
    shortest=None
    for node in graph[start]:
        if node not in path:
            newpath=find_shortest(graph,node,end,path)
            #print newpath
            if newpath:
                if not shortest or len(shortest)>len(newpath):
                    shortest=newpath
    return shortest

def find_paths(graph,start,end,path):
    path = path+[start]
    if start ==end:
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

def find_path(graph,start,end,path):
    path = path+[start]
    if start==end:
        return path
    if start not in path:
        return None
    for node in graph[start]:
        if node not in path:
            newpath = find_path(graph,node,end,path)
            if newpath: return newpath
    return path

def add_vertex(graph,to,node):
    if to not in graph:
        print "no node named " + to
    for n in graph:
        if n==to:
            graph[n]=graph[n]+[node]
    return graph

def add_edge(graph,to,node):
    if (to and node) not in graph:
        print "one or both of those node do not exist in the graph"
    graph[to]=graph[to]+[node]
    graph[node]=graph[node]+[to]
    return graph

graph = {'a':['b','c'],'b':['c','d'],'c':['d'],'d':['c'],'e':['f'],'f':['c']}
#graph['a']=graph['a'] + ['z']
#print graph
path =[]
#print add_vertex(graph,'f','z')
print add_edge(graph,'a','f')
#print find_path(graph,'a','d',path)
