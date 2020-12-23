def knapSack(W,wt,val,n):
    if n == 0 or W == 0:
        return 0
    if (wt[n-1]>W):
        return knapSack(W,wt,val,n-1)
    else:
        return max(val[n-1]+knapSack(W-wt[n-1],wt,val,n-1), knapSack(W, wt, val , n-1))

def knapSackDP(W,wt,val,n):
    K = [[0 for i in range(W+1)] for j in range(n+1)]
    for i in range(n+1):
        for w in range(W+1):
            if i==0 or w==0:
                K[i][w] = 0
            elif wt[i-1] <= w:
                K[i][w] = max(val[i-1] + K[i-1][w-wt[i-1]], K[i-1][w])
            else:
                K[i][w] = K[i-1][w]
    return K[n][W]

#val = [60,100,120]
#wt = [10,20,30]
val = [int(e) for e in input('value:').split()]
wt = [int(e) for e in input('weight:').split()]
W = int(input('max_weight:'))
n = len(val)
print (knapSackDP(W,wt,val,n))
