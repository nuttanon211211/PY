r,c = [int(e) for e in raw_input().split()]
arr = []
for i in range(r):
	a = str(raw_input())
	b = []
	for j in range(c):
		b.append(a[j])
	arr.append(b)
#print(arr)
row  = []
col = []
for i in range(r):
	x = 0
	for j in range(c):
		x += int(arr[i][j])
	row.append(x)
#print(row)
for j in range(c):
	x = 0
	for i in range(r):
		x+= int(arr[i][j])
	col.append(x)
#print(col)

if r < c:
	for i in range(c-r):
		row.append(0)
if c < r:
	for i in range(r-c):
		col.append(0)
		
for i in range(min(r,c),0,-1):
	arr = [0]*max(r,c)
	arr2 = [0]*max(r,c)
	for j in range(max(r,c)):
		if i <= row[j]:
			arr[j] = arr[j-1]+1
		if i <= col[j]:
			arr2[j] = arr2[j-1] + 1
	#print(arr,arr2)
	if max(arr) >= i and max(arr2) >= i :
		print(i)
		exit(0)
	
