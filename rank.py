def SCC(G):
    GT = G_T(G)
    max_to_min_F = DFS_1(GT)
    return DFS_2(G,max_to_min_F)

def G_T(G):
    L = [[] for k in range(len(G))]
    for u in range(len(G)):
        for v in G[u]:
            L[v].append(u)
        return L

def DFS_1(G):
    color = [0]*len(G)
    F = []
    for v in range(len(G)):
        if color[v] == 0:
            DFS_1_R(G,v,color,F)
    return F[::-1]

def DFS_1_R(G,u,color,F):
    color[u] = 1
    for v in G[u]:
        if color[v] == 0:
            DFS_1_R(G,v,color,F)
    F.append(u)

def DFS_2(G,order):
    color = [0]*len(G)
    components = []
    for i in range(len(G)):
        v = order[i]
        if color[v] == 0:
            components.append([v])
            DFS_2_R(G,order[i],color,components[-1])
    return components

def DFS_2_R(G,u,color,tree):
    color[u] = 1
    for v in G[u]:
        if color[v] == 0:
            tree.append(v)
            DFS_2_R(G,v,color,tree)

          



#1111111111111111111111111111111111111111111111111111

import sys
sys.setrecursionlimit(5999)
N,E = [int(e) for e in input().split()]
G = [[] for k in range(N)]
for k in range(E):
    u,v = [int(e) for e in input().split()]
    G[u].append(v)


scc = SCC(G)
cid = [0]*N
for k,c in enumerate(scc):
    for e in c:
        cid[e] = k
G1 = [set() for k in range(len(scc))]
Dg = [0]*len(scc)
for u in range(len(G)):
    for v in G[u]:
        if cid[v] != cid[u] and cid[v] not in G1[cid[u]]:
            G1[cid[u]].add(cid[v])
            Dg[cid[v]] += 1
#===================================================


from collections import deque

rank  = [-1]*len(scc)
for _,s in sorted([(d,v) for v,d in enumerate(Dg)]):
    if rank[s] == -1:
        Q = deque()
        rank[s] =1
        Q.append(s)
        while len(Q) > 0:
            u = Q.popleft()
            for v in G1[u]:
                rank[v] = max(rank[v],rank[u]+1)
                Q.append(v)

cnt = [0]*(max(rank)+1)
for r,c in zip(rank,scc):
    cnt[r] += len(c)
print(*cnt[1:])
