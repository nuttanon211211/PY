def mcm(arr,i,j):
	if i == j:
		return 0
	min = float('inf')
	for e in range(i,j):
		c = mcm(arr,i,e) + mcm(arr,e+1,j) + arr[i-1]*arr[e]*arr[j]
		if c < min:
			min = c
	return min


n = int(input())
arr = [int(e) for e in raw_input().split()]
#print(arr)
print(mcm(arr,1,n-1))
