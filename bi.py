def biFac():
	n = int(input("input number: "))
	k = 1
	p = 0
	while (k<n):
		k *= 2
		p += 1
	while (n!=0):
		if(k>n):
			k /= 2
			p -= 1
		else:
			print(p,k)
			n -=k
			
def biDef():
	n = int(input("input number: "))
	k = 1
	w = ''
	n += 1
	while (k<n):
		k *= 2
	
	while (k!=1):
		k /=2
		if(n>k): 
			w = w+'1'
			n -= k
		else:
			w =w+'0'
	print(w)
	
def biDuo():
	n = float(input("input number:  "))
	N = n
	k = 0.5
	sum = 0.0
	sum2 = 0.0
	ar = []
	w = ''
	w2 = ''
	for i in range(23):
		if(n >=k):
			print("USED",i+1,k)
			n -= k
			sum += k
			w = w + '1'
			ar.append(1)
		else:
			print("NOT USED",i+1,k)
			w = w + '0'
			ar.append(0)
		k /= 2
	print('sum= '+str(sum))
	print('diff= '+str(sum - N))
	print(w)
	print("---Press 1 to calculate upper bound")
	c = raw_input()
	if (c == '1'):
		#print(ar)
		for i in range(22,-1,-1):
			if  ar[i] == 0:
				ar[i] = 1
				for j in range(i+1,23):
					ar[j]=0
				break
			3
		print("calculate :"  )
		for e in ar:
			w2 = w2 + str(e)
		print(w2)
		
		k = 0.5
		for e in ar:
			sum2 += e*k
			k/=2
		#print(ar)
		print("sum= "+str(sum2))
		print("diff= "+str(sum2- N))
	
	
code = 0
while (code != 999):
	print("------  BI CAL -------")
	print("( 1 )       BINARY FACTORIZER")
	print("( 2 )       BINARY DEFINITIZER")
	print("( 3 )       BINARY SMALL FACTORIZER")
	print('( 999 )     QUIT')
	code = int(input('InPUT CODE:'))
	if (code == 1):
		biFac()
	if (code== 2):
		biDef()
	if code == 3:
		biDuo()
