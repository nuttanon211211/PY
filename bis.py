n , q = [int(e) for e in raw_input().split()]
arr = [int(e) for e in raw_input().split()]
questions = [int(e) for e in raw_input().split()]
 
 
def bis (arr,s,e,x):
	if e >= s:
		m = s + (e-s)//2
		if arr[m] == x:
			return m
		
		elif arr[m] > x:
			return bis(arr,s,m-1,x)
		else:
			return bis(arr,m+1,e,x)	
		
	else:
		return -1

for x in questions:
	if x < arr[0]:
		print(-1)
		continue
	ans = bis(arr,0,n,x)
	while(ans == -1):
		x -=1
		ans = bis(arr,0,n,x)
	if ans != n-1:
		while(arr[ans] == arr[ans+1]):
			ans+=1
			if ans == n-1:
				break
		
	print(ans)
