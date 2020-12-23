import math
n,k = [int(e) for e in raw_input().split()]

if k == 1:
	s = ""
	for i in range(1,n+1):
		s += str(i) + " "
	print(s)
	exit(0)
if k%2==0 or k> n*math.log(n,2):
	print("-1")
	exit(0)

