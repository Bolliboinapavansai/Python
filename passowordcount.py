p=input()
count1=int(0)
count2=int(0)
count3= int(0)
a=len(p)
b=['1' , '2' , '3', '4' , '5' , '6' , '7' , '8' , '9' , '0']
if(a >=8 and a <=12):
	for char in p:
		if(char.isupper()):
			count1=count1+1
		elif(char.islower()):
			count2=count2+1
		if(char in b):
			count3= count3+1


if(count1>=2 and count2>=3 and count3>=1):
	print('Valid')
else:
	print('Invalid')