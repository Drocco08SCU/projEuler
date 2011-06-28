from math import sqrt
# def factor(num):
#     hlf = filter(lambda x: num%x==0,range(1,int(sqrt(num))))
#     scnd = []
#     for f in hlf: scnd.append(num/f)
#     return hlf+scnd     

# def factor(n):  
#   yield 1  
#   i = 2  
#   limit = n**0.5  
#   while i <= limit:  
#     if n % i == 0:  
#       yield i  
#       n = n / i  
#       limit = n**0.5  
#     else:  
#       i += 1  
#   if n > 1:  
#     yield n


def genFactors(n):
    yield 1
    for i in xrange(2, n/2 + 1):
        if n % i == 0:
            yield i
            yield n
            
def factor(n):
    return list(genFactors(n))


def findTri(list, facNum):
    mid = len(list)/2
    if len(factor(list[mid])) > facNum:
        findTri(list[:mid],facNum)
    elif len(factor(list[mid])) < facNum:
        findTri(list[mid:],facNum)
    else:
        print mid, list[mid], facNum, factor(list[mid])
        
        

triangles = [0]
n = 1

while n<400000:
    triangles.append(triangles[-1]+n)
    n+=1

print len(factor(triangles[-1]))
print len(factor(triangles[1]))

findTri(triangles[300000:],500)
    
