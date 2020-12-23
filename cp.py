n = int(input())
arr = []
ans = []
for i in range(n):
	a = [int(e) for e in raw_input().split()]
	arr.append(a)

#print(arr)

for i in range(n):
	for j in range(n):
		if i != j:
			ans.append((arr[i][0]-arr[j][0])**2 + (arr[i][1]-arr[j][1])**2)
		
print(min(ans))
		
