import numpy as np
from numpy.linalg import svd


h ,w ,j = [int(e) for e in input().split()]
a = []
for i in range(h):
	temp = [int(e) for e in input().split()]
	a.append(temp)
#print(a)
u , s , vh = np.linalg.svd(a) 
#print("U,S,Vh")
S = np.diag(s)

#SSize = np.size(S)
S1 = np.zeros((h,w))
S2 = np.zeros((w,h))
S1[:,:-1] = S
S2[:-1,:] = S
#print("S1=")
#print(S1)
#print("S2=")
#print(S2)
#print(SSize)
#print("U=")
#print(u)
#print("S=")
#print(S)
#print("Vh=")
#print(vh)
#print("u*S1=")
#print(np.matmul(u,S1))
#print("OUT")
#print(np.matmul(np.matmul(u,S1),vh))
#print("Size of s")
#print(s.size)
sc = np.zeros(s.size)
for i in range(j):
	sc[i] += s[i]
#print("SC")
#print(sc)

Sc = np.diag(sc)
Sc1 = np.zeros((h,w))
Sc1[:,:-1] = Sc
#print("Sc1")
#print(Sc1)
#print("OUT")
ans = np.matmul(np.matmul(u,Sc1),vh)
ans = np.round(ans,0)
#print(ans)
out = list(ans)
o = ''
for e in out:
	tem = ''
	for x in e:
		
		#print(int(x),end=' ')
		tem  = tem + str(int(x))+' '
	#print(tem)
	#print()
	o+=tem.strip()+'\n'
print(o.strip())
