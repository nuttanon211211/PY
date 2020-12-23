def fibo(n):
    a = [0 for i in range(n+1)]
    a[0],a[1] = 0 ,1
    for i in range (2,n+1):
        a[i] = a[i-1] + a[i-2]
    return a[n]
def fiboSlow(n):
    if n==0:  return 0;
    if n==1: return 1;
    return fiboSlow(n-1)+fiboSlow(n-2)


n = int(input())
print("fibo" ,fibo(n))
print("fiboSlow" , fiboSlow(n))
