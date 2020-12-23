import sys
global count = 0






n,k = [int(e) for e in sys.stdin.readline().split()]
g = [[] for i in range(n)]
l = [[0]*k for i in range(k)]

for i in range(n):
    a,b = [int(e)-1 for e  in sys.stdin.readline().split()]
    edge[a].append(b)
