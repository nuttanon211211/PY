import sys
n  = int(sys.stdin.readline())
S = [int(e) for e in sys.stdin.readline().split()]

F = [int(e) for e in sys.stdin.readline().split()]
d = dict()
for i in range(n):
    if F[i] in d:
        if S[i] > d[F[i]] : d[F[i]] = S[i]
    else:
        d[F[i]] = S[i]
count =0
#print(S)
#print(F)
last = float("-inf")
for e in sorted(d.keys()) :
    if d[e] >= last:
        count += 1
        last = e
print(int(count))
        

