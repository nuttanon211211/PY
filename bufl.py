import sys
keyboard = sys.stdin

numOfFood , rangeOfLight , numOfTable = [int(e) for e in keyboard.readline().split()]
foodLocations = [int(e) for e in keyboard.readline().split()]
foodLocations.sort()
thisLocation = 1
count = 0
i=0
while(i<numOfFood):
	if thisLocation < foodLocations[i]:
		thisLocation += 1
	elif thisLocation == foodLocations[i]:
		thisLocation += 2*rangeOfLight + 1
		count += 1
	else:
		i+=1
	
	
print(count)
