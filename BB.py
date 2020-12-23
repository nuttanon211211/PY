import sys
keyboard = sys.stdin

numOfBB = int(keyboard.readline())
BB = [int(e) for e in keyboard.readline().split()]
BB = [0,0,0]+ BB
for i in range(3,numOfBB+3):
	BB[i] = max(BB[i]+BB[i-3],BB[i-1],BB[i-2])
print(BB[numOfBB+2])
