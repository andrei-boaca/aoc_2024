import math
import sys
import copy


ans = 0
while True:
	try:
		v = [i for i in input().split()]
		v = [int(x) for x in v]
		cpy = copy.deepcopy(v)
		cpy.sort()
		revcpy = copy.deepcopy(cpy)
		revcpy.reverse()
		if cpy != v and revcpy != v:
			continue
		ok = 1
		lg = len(v)
		for i in range(0,lg-1):
			val = abs(v[i]-v[i+1])
			if val < 1 or val > 3:
				ok=0
		ans += ok
	except EOFError:
		break

print(ans)

