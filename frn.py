n , e, k = [int(e) for e in input().split()]
g = [[] for i in range(n)]
for i in range(e):
    a,b = [int(e) for e in input().split()]

    g[a].append(b)
    g[b].append(a)
#print(g)
s =set()
sol = []
for i in range(n):
    s.clear()
    s.update(g[i])
    for j in range(k):
        for l in list(s):
            #print("l",l)
            s.update(g[l])
    s.discard(i)
    #print(len(s))
    sol.append(len(s))
print(max(sol))
