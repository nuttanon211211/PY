def tile(startX,startY,Length,X,Y):
	###Only work for size 2
	if Length == 2:
		Bpoint = 2*(Y-startY) + (X-startX)
		print(str(Bpoint)+" "+str(startX)+" "+str(startY))
	
	return 2
	
	
	





def main():
	#print(555)
	Size , ReqX , ReqY = [int(e) for e in input().split()]
	tile(0,0,Size,ReqX,ReqY)
	
	
if __name__ == "__main__":
	main()
