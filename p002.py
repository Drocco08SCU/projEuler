FibNums = [1,2]

def fib(seq):
	seq.append(seq[-1]+seq[-2])
	if seq[-1] + seq[-2] <= 4000000:
		return fib(seq)
	else:
		return seq

FibNums = fib(FibNums)
print FibNums
print filter(lambda x: x % 2 == 0, FibNums)
print reduce(lambda x, y: x + y, filter(lambda x: x % 2 == 0, FibNums))