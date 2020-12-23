size = int(input())
arr = []
ans = [[0]*size]*size
for i in range(size):
	a2 = [int(e) for e in raw_input().split()]
	arr.append(a2)
#print(arr)
#print(ans)
for i in range(size):
	for j in range(size):
		if i-1 >= 0 and j-1 >= 0:
			ans[i][j] = max(arr[i][j],arr[i-1][j-1],arr[i-1][j-1]+arr[i][j])
		else:
			ans[i][j] = arr[i][j]
#print(ans)
max = ans[0][0]
for e in ans:
	for x in e:
		if x > max:
			max = x
print(max)
