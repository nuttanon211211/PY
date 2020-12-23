

n ,k = [int(e) for e in raw_input().split()]
#array n,k [n][k]
arr = [0] * (k+1)
arr2 = [0] * (k+1)
arr[1] = 1
arr2[1] = 1


for i in range(2,n+1):
	for j in range(2,k+1):
		arr2[j] = ((arr[j]%1997)*(j%1997) + arr[j-1]) %1997
	arr ,arr2 = arr2,arr
print(arr[k])


