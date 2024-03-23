month=int(input())
day=int(input())
if(month==2 and day==18):
    print('special')
elif(day>18 and month>=2):
    print('after')
elif(month<=2 and day<18):
    print('before')