alpha = range(101)

def sumOFsquares(list):
	return reduce(lambda x,y:x+y**2,list)

def squareOFsums(list):
	return reduce(lambda x,y:x+y,list)**2
	
print sumOFsquares(alpha) 
print squareOFsums(alpha)
print squareOFsums(alpha) - sumOFsquares(alpha)