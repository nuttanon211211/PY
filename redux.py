def binary_search(a, item, low, high): 
	if low == high: 
		if a[low] > item: 
			return low
		else: 
			return low+1
	if low > high: 
		return low
	mid = (low+high)/2
	if a[mid] < item: 
		return binary_search(a, item, mid+1, high) 
	elif a[mid] > item: 
		return binary_search(a, item, low, mid-1) 
	else: 
		return mid 

def insertion_sort(arr): 
	for i in xrange(1, len(arr)): 
		val = arr[i] 
		j = binary_search(arr, val, 0, i-1) 
		arr = arr[:j] + [val] + arr[j:i] + arr[i+1:] 
		#print(arr)
	return arr 

print insertion_sort([123,1,421,89,79,55,50,21,19,3]) 

