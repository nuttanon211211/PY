def fibonucci(n):
    fibo = [0 for i in range(1000)]
    fibo[1] = 1
    fibo[2] = 1
    for i in range(3,n+1):
        fibo[i] = fibo[i-1] + fibo[i-2]
    return fibo


for i in range(1,101):
    print(fibonucci(i))

