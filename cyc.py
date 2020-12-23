from collections import defaultdict
class Graph():
    def __init__(self,vertices):
        self.graph = defaultdict(list)
        self.V = vertices
    def addEdge(self,u,v):
        self.graph[u].append(v)
    def isCyclicUtil(self,v,visited,recStack):
        visited[v] = True
        recStack[v] = True

        for neighbour in self.graph[v]:
            if visited[neighbour] == False:
                if self.isCyclicUtil(neighbour,visited, recStack) == True:
                    return True
            elif recStack[neighbour] == True:
                return True

        recStack[v] = False
        return False
    def isCyclic(self):
        visited = [False] * self.V
        recStack = [False] * self.V
        for node in range(self.V):
            if visited[node] == False:
                if self.isCyclicUtil(node,visited,recStack) == True:
                    return True
        return False

N = int(input())
for i in range(N):
    n,e = [int(e) for e in input().split()]
    g = Graph(n)
    for j in range(e):
        a,b = [int(e) for e  in input().split()]
        g.addEdge(a,b)
    if g.isCyclic():
        print("YES")
    else:
        print("NO")
'''g = Graph(n)
#g.addEdge(0,1)
#g.addEdge(0,2)
#g.addEdge(1,2)
#g.addEdge(2,0)
#g.addEdge(2,3)
#g.addEdge(3,3)
if g.isCyclic() == 1:
    print("Graph has a cycle")
else:
    print("Graph has no cycle")'''
                    
