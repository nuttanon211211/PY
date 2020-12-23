import sys
def isSubsetSum (arr,n,sum):
	if sum == 0:
		return True
	if sum < 0:
		return False
	if n == 0 and sum != 0:
		return False
	
	if arr[n-1] > sum:
		return isSubsetSum(arr,n-1,sum)
		
	return isSubsetSum(arr,n-1,sum) or isSubsetSum(arr,n-1,sum-arr[n-1])
	

def findPartition(arr,n):
	sum = 0
	for i in range(n):
		sum += arr[i]
	if sum%2 != 0:
		return False
	
	return isSubsetSum(arr,n,sum//2)
	
# Program
#print("INPUT ARR.")
#arr = [int(e) for e in sys.stdin.readline().split()]
#n = len(arr)
arr = []
n =0
for i in range(1,101):
	arr.append(i*1000)
	n += 1
	
	
	if findPartition(arr,n) == True:
		print(arr,n,"TRUE")
	else:
		print(arr,n ,"FALSE")
