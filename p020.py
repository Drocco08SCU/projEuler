from math import factorial
print reduce(lambda x,y: int(x)+int(y), str(int(factorial(100))))