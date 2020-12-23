import math
a = [int(e) for e in raw_input().split()]
b = [int(e) for e in raw_input().split()]
c = [int(e) for e in raw_input().split()]

def angle(x1,x2,x3,y1,y2,y3,z1,z2,z3):
	num = (x2-x1)*(x3-x1) + (y2-y1)*(y3-y1) + (z2-z1)*(z3-z1)
	den = math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2) * math.sqrt((x3-x1)**2 + (y3-y1)**2 + (z3-z1)**2)
	angle = math.degrees(math.acos(num/den))
	return round(angle,6)
	
	
#print(angle(a[0],a[1],a[2],b[0],b[1],b[2],c[0],c[1],c[2]))
#print(angle(a[1],a[0],a[2],b[1],b[0],b[2],c[1],c[0],c[2]))
#print(angle(a[2],a[1],a[0],b[2],b[1],b[0],c[2],c[1],c[0]))
Angle = angle(a[0],b[0],c[0],a[1],b[1],c[1],a[2],b[2],c[2])
print("%.6f" % Angle)

def area(p1,p2,p3,q1,q2,q3,r1,r2,r3):
	A = (q1-p1)**2 + (q2-p2)**2 + (q3-p3)**2
	B = (r1-q1)**2 + (r2-q2)**2 + (r3-q3)**2
	C = (p1-r1)**2 + (p2-r2)**2 + (p3-r3)**2
	stSq = 4*A*B - (C-A-B)**2
	S =  math.sqrt(stSq/16)
	return round(S,6)

def area2(x1,x2,x3,y1,y2,y3,z1,z2,z3,Angle):
	
	#print(Angle)
	SizeA = math.sqrt((z1-x1)**2 + (z2-x2)**2 + (z3-x3)**2) 
	SizeB = math.sqrt((y1-x1)**2 + (y2-x2)**2 + (y3-x3)**2)
	A = 0.5 * SizeA * SizeB * math.sin(math.radians(Angle))
	return round(A,6)
	
Area = area2(a[0],a[1],a[2],b[0],b[1],b[2],c[0],c[1],c[2],Angle)
print("%.6f" % Area)

def minimize(x1,x2,x3):
	if x1 == 1:
		return (x1,x2,x3)
	else:
		inverse = float(1.0/float(x1))
		#print(inverse)
		return (x1*inverse , x2 * inverse , x3 * inverse)

def ortho(x1,x2,x3,y1,y2,y3,z1,z2,z3):
	u1,u2,u3 = y1-x1 , y2-x2 , y3-x3
	v1 ,v2,v3 = z1-x1 , z2-x2 ,z3-x3
	(u1 , u2 , u3) = minimize(u1,u2,u3)
	(v1 , v2 , v3) = minimize(v1,v2,v3)
	#print(u1,u2,u3)
	#print(v1,v2,v3)
	w2 = u2+v2
	w3 = u3+v3
	# x = my  , how many times that x greater than y
	m = (v3-u3) / (u2-v2)
	w2 *= m  # change to y
	# w2y + w3y = -2
	y = -2/(w2+w3)
	x = m*y
	return (round(1,6),round(x,6),round(y,6))
	
(a,b,c) = ortho(a[0],a[1],a[2],b[0],b[1],b[2],c[0],c[1],c[2])
print("%.6f" % a +" "+ "%.6f" % b +" "+ "%.6f" % c)
