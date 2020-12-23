from math import gcd

def lcm(array):
	LCM = array[0]
	for e in array[1:]:
		LCM = int(LCM*e/gcd(LCM,e))
	return LCM

def divideSum(arr,N):
	count = 0
	for e in arr:
		count += N//e
	return count

#print(lcm([2,3,5]))

#print("Plaese type  Seat Capacity and Number of question customer do you want to know? : [ S N ]")
numberOfSeat , attendeeNumber = [int(e) for e in input().split()]
#print("input Cheftime(array) size is equal to Seat Capatity.")
ChefTime = [int(e) for e in input().split()]
#print("Which customer do you want to know?(equal num of qeustion) ewe")
WhichCustomer = [int(e)-1 for e in input().split()]
CycleChef = lcm(ChefTime)
#print("Cycle of chef =")
#print(CycleChef)
#print("Number of customer per cycle is")
CustomerPerCycle = divideSum(ChefTime,CycleChef)
#print(CustomerPerCycle)
Waitingtime = [0]*(CustomerPerCycle)
#print("Waiting time for each customer that dont exceed the cycle=")
#print(Waitingtime)
seatCountDown = [0]*numberOfSeat
person = 0
for t in range(CycleChef):
	for i in range(numberOfSeat):
		if seatCountDown[i]==0:
			Waitingtime[person] = t
			person += 1
			seatCountDown[i] = ChefTime[i]
		seatCountDown[i] -= 1
	
#print("Waiting time for each customer that dont exceed the cycle=")
#print(Waitingtime)
for e in WhichCustomer:
	if e < CustomerPerCycle:
		print(Waitingtime[e])
	else:
		Cycle = e//CustomerPerCycle
		customerThing = e % CustomerPerCycle
		
#		print("Cycle="+str(Cycle))
#		print("CycleChef="+str(CycleChef))
#		print("Divided Customer="+str(customerThing))
		
		print(Waitingtime[customerThing] + Cycle*CycleChef)



	
	 
