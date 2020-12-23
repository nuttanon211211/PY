n = int(input())
arr = [int(e) for e in input().split()]
L = []
for i in range(n):
    if i == 0:
        L.append(arr[i])
    elif i == 1:
        L.append(arr[i] + L[i-1])
    elif i == 2:
        L.append(arr[i] + max(L[i-1],L[i-2]))
    else:
        L.append(arr[i] + max(L[i-1],L[i-2],L[i-3]))
    #print(L[-1])
print(L[-1])
