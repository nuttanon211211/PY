import sys
import math

def long(n):
    return 2**(int(math.log(n,2)) + 1) - 1

def weAreNumberOne(n,l,r,mem):
    if (l > r): return 0
    if (n==0): return 0
    if (n==1): return 1
    if (n,l,r) in mem: return mem[(n,l,r)]
    m = long(n//2) 
    if r < m+1:
        c = weAreNumberOne(n//2,l,r,mem)
    elif l > m+1:
        c = weAreNumberOne(n//2,l-m-1,r-m-1,mem)
    else:
        c = weAreNumberOne(n//2,l,m,mem) + n%2 + weAreNumberOne(n//2,1,r-m-1,mem)
    mem[(n,l,r)] = c
    return c
    
    
    

n , l , r = [int(e) for e in sys.stdin.readline().split()]
print(weAreNumberOne(n,l,r,dict()))

