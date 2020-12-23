n,v = [int(e) for e in raw_input().split()]
coins = [int(e) for e in raw_input().split()]
arr = [float('inf')]*(v+1)
arr[0] = 0
for coin in coins:
	for x in range (coin , v+1):
		arr[x] = min(arr[x],arr[x-coin] + 1)
print(arr[v])


