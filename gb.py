import sys
N , E , s = [int(e) for e in sys.stdin.readline().split() ]

g = {}

for i in range(N):
    g[i] = []
for i in range(E):
     a, b,c = [int(e) for e in sys.stdin.readline().split()]
     g[a].append((b,c))

INF = float('inf')
d = [INF for i in range(N)]
p = [None for i in range(N)]

def BF(g,s):
    d[s] = 0
    for i in range(N+1):
        No = False
        for u in g:
            for (v,w) in g[u]:
                if (d[u]+w < d[v]):
                    d[v] = d[u] +w
                    p[v] = u
                    No = True
    if No:
        return None,None
    return d,p

d, p  = BF(g,s)
if d == None:
    print(-1)
else:
    for i in d:
        print(i,end=" ")
            
