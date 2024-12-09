import math
import sys
import copy


def safe(v):
	cpy = copy.deepcopy(v)
	cpy.sort()
	revcpy = copy.deepcopy(cpy)
	revcpy.reverse()
	if cpy != v and revcpy != v:
		return 0
	ok = 1
	lg = len(v)
	for i in range(0,lg-1):
		val = abs(v[i]-v[i+1])
		if val < 1 or val > 3:
			ok=0
	return ok

def good(v):
	lg = len(v)
	for i in range(0,lg):
		aux = []
		for j in range(0,lg):
			if j != i:
				aux.append(v[j])
		if safe(aux):
			return 1
	return 0


ans = 0
while True:
	try:
		v = [i for i in input().split()]
		v = [int(x) for x in v]
		ans += good(v)
	except EOFError:
		break

print(ans)

