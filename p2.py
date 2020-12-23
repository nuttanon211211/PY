#import numpy as np

def appendRank(a):
	if (a[0]==0):
		if (a[1]==0):
			if (a[2]==0):
				a.append(0)
			else:
				a.append(1)
		else:
			a.append(2)
	else:
		a.append(3)

def checkRank(a):
	if (a[0]==0):
		if (a[1]==0):
			if (a[2]==0):
				a[4] = 0
			else:
				a[4] = 1
		else:
			a[4] = 2
	else:
		a[a] = 3

def Rank(a):
	return a[4]
	
def minimize(a):
	if a[0] == 1 or a[0]==0:
		return a
	else:
		inverse = 1.0/a[0]
		return [a[0]*inverse,a[1]*inverse,a[2]*inverse,a[3]*inverse,a[4]]
		
def subtract(a,b):
	return [a[0]-b[0],a[1]-b[1],a[2]-b[2],a[3]-b[3],a[4]]
	
def minimize2(a):
	if a[1]==1 or a[1]==0:
		return a
	else:
		inverse = 1.0/a[1]
		return [a[0]*inverse,a[1]*inverse,a[2]*inverse,a[3]*inverse,a[4]]
		
		
def minimize3(a):
	if a[2]==1 or a[2]==0:
		return a
	else:
		inverse = 1.0/a[2]
		return [a[0]*inverse,a[1]*inverse,a[2]*inverse,a[3]*inverse,a[4]]
			
			
a = [float(e) for e in input().split()]
b = [float(e) for e in input().split()]
c = [float(e) for e in input().split()]
ans = [60*int(e) for e in input().split()]
c.append(c[-1])
d = [a[0],b[0],c[0],ans[0]]
e = [a[1],b[1],c[1],ans[1]]
f = [a[2],b[2],c[2],ans[2]]


appendRank(d)
appendRank(e)
appendRank(f)
#print("InINit")
#print(d)
#print(e)
#print(f)
#exit(0)


d = minimize(d)
e = minimize(e)
f = minimize(f)
#print("Aft MINIMIZE")
#print(d)
#print(e)
#print(f)

if(Rank(d)!=3):
	if(Rank(e)!=3):
		d,f = f,d
	else:
		d,e = e,d

#print("AFT SWAP")
#print(d)
#print(e)
#print(f)	


if Rank(e) == 3:
	e = subtract(e,d)
if Rank(f) == 3:
	f = subtract(f,d)
checkRank(e)
checkRank(f)

#print("AFT SUBSrART")
#print(d)
#print(e)
#print(f)


		
e = minimize2(e)
f = minimize2(f)

#print("AFT MINIM")
#print(d)
#print(e)
#print(f)

if(Rank(e)!=2):
	e,f = f,e

#print("AFT SWAP")
#print(d)
#print(e)
#print(f) 


if Rank(f)== 2:
	f = subtract(f,e)
checkRank(f)

#print("AFT SUBSTr")
#print(d)
#print(e)
#print(f) 

f = minimize3(f)

Z = f[3]
Y = e[3] - Z*e[2]
X = d[3] - Y*d[1] - Z*d[2]
#print("x,y,z")
print("%.3f %.3f %.3f"%(X,Y,Z))
	


