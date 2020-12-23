import sys
keyboard = sys.stdin

count = 0
def findNumOfSubSpecDist(startNode,distanceOfAnswer):
	global count 
	listData[startNode][0] = 1
	for i in range(len(edgeData[startNode])):
		nextNode = edgeData[startNode][i]
		findNumOfSubSpecDist(nextNode,distanceOfAnswer)
		for j in range(distanceOfAnswer):
			count += listData[startNode][j] * listData[nextNode][distanceOfAnswer-j-1]
		for j in range(distanceOfAnswer):
			listData[startNode][j+1] += listData[nextNode][j]
	
	
numOfNode, distanceOfAnswer = [int(e) for e in keyboard.readline().split()]
edgeData = [[] for i in range(numOfNode+1)]
for i in range(1,numOfNode):
	firstNode , secondNode = [int(e) for e in keyboard.readline().split()]
	edgeData[firstNode].append(secondNode)

listData = [[0]*(distanceOfAnswer+1) for i in range(numOfNode+1)]
findNumOfSubSpecDist(1,distanceOfAnswer)

print(count)
