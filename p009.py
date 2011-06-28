import sys
for a in range(1,500):
	for b in range(a,500):
		c = 1000-a-b
		if (a**2+b**2==c**2) and (a+b+c==1000):
			sys.exit(str(a*b*c))