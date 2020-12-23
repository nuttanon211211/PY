import sys

def findPartition(arr,n):
	sum = 0
	i,j= 0,0
	
	for i in range(n):
		sum+= arr[i]
	
	if sum%2 !=0:
		return False
	
	PART = [[True for i in range(n+1)] for j in range(sum//2 +1)]
	
	for i in range(n+1):
		PART[0][i] = True
	
	for i in range(1,sum//2 +1):
		PART[i][0] = False
	
	for i in range(1,sum//2 +1):
		for j in range(1,n+1):
			PART[i][j] = PART[i][j-1]
			
			if i >= arr[j-1]:
				PART[i][j] = PART[i][j] or PART[i-arr[j-1]][j-1]
	return PART[sum//2][n]
	
	
# Program
#print("INPUT ARR.")
#arr = [int(e) for e in sys.stdin.readline().split()]
#n = len(arr)
arr = []
fibo = [0]*100;
n=0;
v = 3;

fibo[1] = 1
fibo[2] = 1
for i in range(3,100):
	fibo[i] = fibo[i-1]+fibo[i-2] 
print(fibo)
for i in range(1,21):
	arr.append(v)
	n += 1
	v *=2
	
	
	if findPartition(arr,n) == True:
		print(arr,n,"TRUE")
	else:
		print(arr,n ,"FALSE")
