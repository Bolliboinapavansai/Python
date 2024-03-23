a=int(input())
b=int(input())
c=int(input())
if(a>b and a>c):
	if(b>c):
		print(b)
	else:
		print(c)
elif(b>a and b>c):
	if(c>a):
		print(c)
	else:
		print(a)
elif(c>a and c>b):
	if(a>b):
		print(a)
	else:
		print(b)