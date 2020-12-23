import sys
import heapq
numOfStars , numOfMassRelays , numOfQuestions = [int(e) for e in sys.stdin.readline().split()]
starData = []
for i in range(numOfMassRelays):
	firstStarSystem , secondStarSystem , starDistance = [int(e) for e in sys.stdin.readline().split()]
	starData.append((starDistance,firstStarSystem,secondStarSystem))
starData.sort()
points = [i for i in range(numOfStars)]
heap = [0]*numOfStars
answer = [0]*numOfStars
for i in range(numOfMassRelays):
	starDistance , firstStarSystem , secondStarSystem = starData[i][0],starData[i][1],starData[i][2]
	while firstStarSystem != points[firstStarSystem]:
		firstStarSystem = points[firstStarSystem]
	while secondStarSystem != points[secondStarSystem]:
		secondStarSystem = points[secondStarSystem]
	if firstStarSystem != secondStarSystem:
		if heap[firstStarSystem] < heap[secondStarSystem]:
			points[firstStarSystem] = secondStarSystem
		elif heap[firstStarSystem] > heap[secondStarSystem]:
			points[secondStarSystem] = firstStarSystem
		else:
			points[secondStarSystem] = firstStarSystem
			heap[firstStarSystem] +=1
		numOfStars -=1
		answer[numOfStars] = starDistance
	
for i in range(numOfQuestions):
	print(answer[int(sys.stdin.readline())])	


	
