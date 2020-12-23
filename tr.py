n = int(input())
arr = [[int(e) for e in raw_input().split()] for i in range(n)]
for i in xrange(1,n):
	arr[i][0] += arr[i-1][0]
	for j in xrange(1,i):
		arr[i][j] += max(arr[i-1][j-1],arr[i-1][j])
	arr[i][i] += arr[i-1][i-1]
#print(arr)
print(max(arr[n-1]))
