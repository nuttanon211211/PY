def thereNoUser(arr,user):
	#arr is [[value,user] ...]
	for e in arr:
		if e[1] == user:
			return 0
	return 1

def removeAuction(arr,user):
	targetIndex = -1
	for i in range(len(arr)):
		if (arr[i][1] == user):
			targetIndex = i
			break
	if targetIndex != -1:
		arr.pop(targetIndex)
	
	




N , M , A = [int(e) for e in raw_input().split()]
data = dict()
userGet = list()
for i in range(M+1):
	userGet.append([])
print(userGet)
temp = [int(e) for e in raw_input().split()]
for i in range(1,N+1):
	data[i] = list()
	data[i].append(temp[i-1])
	data[i].append(list())
print(data)
for i in range(A):
	code = [e for e in raw_input().split()]
	print(code)
	if code[0] == 'B':
		user = int(code[1])
		itemNumber = int(code[2])
		value = int(code[3])
		#pair [value,user] in data[itemNum][1] , data[itemNum][0] is remaining
		if( thereNoUser(data[itemNumber][1],user) == 1 ):
			data[itemNumber][1].append([value,user])
		else:
			removeAuction(data[itemNumber][1],user)
			data[itemNumber][1].append([value,user])
			
	if code[0] == 'W':
		user = int(code[1])
		itemNumber = int(code[2])
		if( thereNoUser(data[itemNumber][1],user) == 0 ):
			removeAuction(data[itemNumber][1],user)
			
print(data)
for i in range(1,N+1):
	data[i][1].sort()
print(data)
for i in range(1,N+1):
	if(len(data[i][1]) != 0):
		if(data[i][0] > 0):
			temp = data[i][1].pop()
			print(temp)
			# temp is [value ,user]
			print(temp[1])
			userGet[temp[1]].append(str(i))
			data[i][0] -= 1
print(userGet)
for i in range(1,M+1):
	if len(userGet[i]) > 0:
		print(' '.join(userGet[i]))
		
	else:
		print('NONE')
	
			
		
