numberOfElement = int(input())
array = [int(e) for e in input().split()]
count = 0
for i in range(numberOfElement):
	for j in range(i+1,numberOfElement):
		if array[i] > array[j]:
			count += 1
print(count)
		
