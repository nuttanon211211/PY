n,k = [int(e) for e in raw_input().split()]
arr = [int(e) for e in raw_input().split()]

arr2 = [float('inf')]*n
for i in range(n):
	if i <= k:
		arr2[i] = min(arr2[i],arr[i])	
	if i > 1:
		arr2[i] = min( arr2[i] , min(arr2[max(0,i-1-2*k):i]) + arr[i] )
#print(arr2)
print(min(arr2[-1-k:]))
