n = int(input())
arr = [int(e) for e in raw_input().split()] 
global maxx
maxx = 1
def lis(arr,n):
	global maxx
	if n == 1:
		return 1
	maxe = 1
	for i in xrange(1,n):
		res = lis(arr,i)
		if arr[i-1] < arr[n-1] and (res + 1)>maxe:
			maxe = res+1
	maxx = max(maxx,maxe)
	return maxe
	
lis(arr,n)
print(maxx)
