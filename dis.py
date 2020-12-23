import sys,heapq
row ,col = [int(e) for e in sys.stdin.readline().split()]
matr = [[int(e) for e in sys.stdin.readline().split()] for i in range(row)]
dij = [[float("inf")]*col for i in range(row) ]
#print(dij)
dij[0][0] = 0
Heap = [(0,0,0)]
while len(Heap) > 0:
	w,u,v = heapq.heappop(Heap)
	for i,j in ((-1,0),(0,-1),(1,0),(0,1)):
		x = u+i 
		y = v+j
		if 0<=x<row and 0<=y<col and matr[x][y]+w < dij[x][y]:
			dij[x][y] = matr[x][y] + w
			heapq.heappush(Heap,(dij[x][y],x,y))

for e in dij:
	dis = ""
	for w in e:
		dis = dis + " " + (str)(w);
	print(dis.strip())
