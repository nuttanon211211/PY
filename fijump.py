
MAX = 1e9
def fijump(arr,n):
    fib =[0 for i in range (30)]
    fib[0] = 0
    fib[1] = 1
    for i in range (2,30):
        fib[i] = fib[i-1]+fib[i-2]
    DP = [0 for i in range( n + 2 )]
    DP[0] = 0
    for i in range(1,n+2):
        DP[i] = MAX
    for i in range(1,n+2):
        for j in range(1,30):
            if (arr[i-1]==1 or i == n+1) and i-fib[j] >=0:
                DP[i] = min(DP[i], 1 + DP[i-fib[j]])
    if (DP[n+1] != MAX):
        return DP[n+1]
    else:
        return -1
arr = [int(e) for e in sys.stdin.readline()]
n = len(arr)
print(fijump(arr,n-1))
