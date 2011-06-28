def is_prime(n):
	import math
    n = abs(n)
    i = 2
    while i <= math.sqrt(n):
        if n % i == 0:
            return False
        i += 1
    return True

alpha = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
primeFactor = 19*17*13*11*7*5*3*2*1
i = primeFactor
while ([x for x in alpha if i%x!=0] != []):
	# print i, [x for x in alpha if i%x==0]
	i+=primeFactor
print "Found it! :::  " + str(i)
	