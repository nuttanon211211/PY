n,a,b,c = [int(e) for e in raw_input().split()]
arr = [0]*(n+1)
#print(arr)
a,b,c = sorted([a,b,c])
arr[a] = 1
#print(a,b,c)
for i in range(a+1,n+1):
	if i%a == 0:
		arr[i] = i//a
	else:	
		arr[i] = max(arr[max(0,i-b)]+1,arr[max(0,i-c)]+1)
#print(arr)
print(arr[n])
