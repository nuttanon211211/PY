import math
n = int(input())
arr = []

for i in range(n):
	a2 = [int(e) for e in raw_input().split()]
	arr.append(a2)
#print(arr)
pareto = [0]*n
value = [0]*n
for i in range(10001):
	maxx = -1
	lo = -1
	for j in range(n):
		value[j] = (arr[j][1]*math.sin(i/10000*math.pi/2)) + arr[j][0]*math.cos((10000-i)/10000*math.pi/2)
#		print(v)
		if value[j] > maxx:
			maxx = value[j]
			lo = j
	for j in range(n):
		if maxx == value[j]:
			pareto[j] = 1
	#pareto[lo] = 1
#print(pareto)
print(sum(pareto))
	
	
