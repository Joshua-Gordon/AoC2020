from typing import Dict, List, Set, Tuple
import re
from collections import defaultdict
from math import ceil
import sys

input = open(sys.argv[1]).readlines()
mem = defaultdict(lambda: 0)
posmask = 0
negmask = 0
xmask = 0

# powerset implementation from https://stackoverflow.com/questions/18035595/powersets-in-python-using-itertools
from itertools import chain, combinations

def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

part = 2

for line in input:
	target, _, value = line.split(" ")
	if target == "mask":
		posmask = int(value.replace("X", "0"), 2)
		negmask = int(value.replace("1", "X").replace("0", "1").replace("X", "0"), 2)
		xmask = int(value.replace("1", "0").replace("X", "1"), 2)
	else:
		if part == 2:
			pos = int(target[4:-1])
			pos |= posmask
			val = int(value)

			posit = []

			for i in range(36):
				if ((1 << i) & xmask) > 0:
					posit.append(i)

			for option in powerset(posit):
				diff = 0
				for bit in option:
					diff |= (1 << bit)
				mem[pos ^ diff] = val
		else:
			pos = int(target[4:-1])
			val = int(value)
			val = (val | posmask) & ~negmask
			mem[pos] = val

ans = 0
for k, v in mem.items():
	ans += v
print(ans)
