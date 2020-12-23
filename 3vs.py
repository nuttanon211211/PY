import sys

n = int(sys.stdin.readline())
data = [int(e) for e in sys.stdin.readline().split()]
count = 0
for i in range(n-1):
    if (data[i+1]==1 and data[i] != 1):
        count +=1
for i in range(n):
    if(data[i]==1):
        data[i] = 2
for i in range(n-1):
    if(data[i+1]==2 and data[i] == 3):
        count += 1
print(count)
