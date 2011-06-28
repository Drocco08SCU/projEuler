possibles=[]

for x in range(999,99,-1):
	for y in range(999,99,-1):
		if str(x*y) == str(x*y)[::-1]:
			possibles.append(x*y)
			
print max(possibles)