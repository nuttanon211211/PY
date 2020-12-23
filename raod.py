n = int(input())
arr = []
used = [0]*n
sum = 0
for i in range(n):
	arr.append(int(input()))
#print(arr)
#print(used)
used[0] = 1
first = used[0]
for k in range(n):
	max = 0
	jlo = 0	
	for i in range(n):
		
		for j in range(n):
			if (i != j and used[i] == 1 and used[j] == 0):
				if(arr[i] ^ arr[j] > max):
					max = arr[i] ^ arr[j]
					jlo = j
	used[jlo] = 1
	sum += max
	
		
print(sum)
