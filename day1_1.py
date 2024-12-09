#!/usr/bin/env python3

import math
import sys

v1 = []
v2 = []

while True:
	try:
		a,b = input().split()
		a=int(a)
		b=int(b)
		v1.append(a)
		v2.append(b)
	except EOFError:
		break
		
v1.sort()
v2.sort()
lg = len(v1)

ans=0
for i in range(0,lg):
	ans += abs(v1[i]-v2[i])

print(ans)
