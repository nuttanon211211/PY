import sys

keyboard = sys.stdin

def currencyAnalysis():
	numOfCurrency = int(keyboard.readline())
	currencyData = []
	for i in range(numOfCurrency):
		currencyData.append([float(e) for e in keyboard.readline().split()])
	for i in range(numOfCurrency):
		for j in range(numOfCurrency):
			for k in range(numOfCurrency):
				currencyData[i][j] = max(currencyData[i][k]*currencyData[k][j],currencyData[i][j])
					
				if currencyData[i][i] > 1:
					print("YES") 
					return
	
	print("NO")
	return			
	print(currencyData)
	
	

numOfQuestions = int(keyboard.readline())
for i in range(numOfQuestions):
	currencyAnalysis()
		
	

		
