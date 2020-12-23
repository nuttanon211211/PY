import sys
def scs(x,y):
    m = len(x)
    n = len(y)
    if (m == 0): return n
    if (n == 0): return m
    if x[m-1] == y[n-1]: return 1+scs(x[:m-1],y[:n-1])
    return 1+min(scs(x[:m-1],y),scs(x,y[:n-1]))

#x = 'abcbdab'
#y = 'bdcaba'
x,y = [e.strip() for e in input().split()]
print(scs(x,y))
