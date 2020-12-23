import numpy as np
from numpy.linalg import eig
from sympy import *

def det2(a):
	return a[0][0]*a[1][1] - a[0][1]*a[1][0]

def det3(a):
	x= [ [a[1][1],a[1][2]] , [a[2][1],a[2][2]] ]
	y= [ [a[1][0],a[1][2]] , [a[2][0],a[2][2]] ]
	z= [ [a[1][0],a[1][1]] , [a[2][0],a[2][1]] ]
	#print(x,y,z)
	return a[0][0]*det2(x)-a[0][1]*det2(y)+a[0][2]*det2(z)
	
def det(a):
	if len(a)==2:
		return det2(a)
	else:
		return det3(a)

def reduce(a):
	inverse = 1.0/a[0]
	for i in range(len(a)):
		a[i]*= inverse
	return a

def summarize(a):
	if len(a)==1:
		count = 0
		temp =a[0][0]
		for i in range(len(a[0])):
			if a[0][i] == temp:
				count += 1
		if count == len(a[0]):
			for i in range(len(a[0])):
				a[0][i] = 1
		return a
	else:
		size = len(a)
		for e in a:
			e = reduce(e)
		return a

def roundSet(a):
	for e in a:
		for i in range(len(e)):
			e[i] = round(e[i],3)
	return a

def setZero(a):
	if (-0.0005<a<0.0005):
		return 0.0
	else:
		return a


a = [float(e) for e in input().split()]
Size = len(a)
A = list()
A.append(a)
for e in range(Size-1):
	temp = [float(e) for e in input().split()]
	A.append(temp)

#print(A)
Anp = np.array(A)
values , vectors = eig(Anp)
print("%.3f"%det(A))
#print(values)
#print(vectors)
data = set()
data2 = dict()

for i in range(Size):
	#print(values[i])
	#print(vectors[:,i])
	#temp = []
	#temp.append(values[i])
	#temp.append(list(vectors[:,i]))
	data.add(round(values[i],3))
	if round(values[i],3) not in data2:
		data2[round(values[i],3)] = [list(vectors[:,i])]
	else:
		data2[round(values[i],3)].append(list(vectors[:,i]))
	
data = list(data)	
data.sort()
data = data[::-1]	
#print(data)
#print(data2)

for v,e in data2.items():
	e = roundSet(e)
	#e = summarize(e)
	M = Matrix(e)
	Mrref = M.rref()
	#print(Mrref[0])
	data2[v]= list(Mrref[0])

#print(data2)
for e in data:
	e = setZero(e)
	print("%.3f"%e)
	count = 0
	for x in data2[e]:
		count += 1
		x = float(x)
		print("%.3f"%x,end=' ')
		if count%Size == 0:
			print()
			
			
