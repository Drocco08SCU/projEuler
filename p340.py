import sys, math
global a,b,c,n
# a = 21**7
a = 1801088541
# b = 7**21
b = 558545864083284007
# c = 12**7
c = 35831808
# num = 2000


def F(n):
	if n>b:
		return n-c
	else:
		return F(a+F(a+F(a+F(a+n))))
		
	

def S(alpha,beta,gamma):
	result = 0
	for n in range( beta+1 ):
		result += F(n)
	return result
	
# print S(a,b,c)
# print F(num)
print S(a,b,c)
# print crazy(2000)