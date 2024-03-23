a=str(input())
b=':-)'
c=':-('
counterb=a.count(b)
print(counterb)
counterc=a.count(c)
print(counterc)
if(counterb>counterc):
	print('happy')
elif(counterb==counterc and counterb and counterc >1):
	print('unsure')
elif(counterc>counterb):
	print('sad')
elif(counterb==counterc==0):
	print('none')