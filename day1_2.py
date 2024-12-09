import math
import sys

mydict = {}

v1=[]
v2=[]
while True:
	try:
		a,b=input().split()
		a=int(a)
		b=int(b)
		v1.append(a)
		v2.append(b)
	except EOFError:
		break

v1.sort()
v2.sort()

for i in v2:
	if i in mydict:
		mydict[i] = mydict[i] + 1
	else:
		mydict[i] = 1
		
ans = 0
for i in v1:
	if i in mydict:
		ans += mydict[i]*i

print(ans)
