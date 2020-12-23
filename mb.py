import sys

point , day = [int(e) for e in sys.stdin.readline().split()]
locations = [int(e) for e in sys.stdin.readline().split()]
peak = locations[-1]
startday = peak // day
days = 0
currentlo = 0
i = 0
while(1):
    currentlo = 0
    days = 0
    while(days<day):
        currentlo += startday
        for i in range(point):
            if(locations[i]>currentlo):
                currentlo = locations[i-1]
                break
        days+=1
        if(currentlo>= peak):
            if(days <= day):
                print(startday,days)
                exit(0)
        
            
    
    startday += 1
    #print(startday)
