def p14(n,cnt):
    if n == 1:
        return cnt
    elif n%2 == 0:
        cnt+=1
        n=n/2
        return p14(n,cnt)
    else:
        cnt+=1
        n = 3*n+1
        return p14(n,cnt)        



high = 10
counts = [0]
for x in range(1,1000000):
    counts.append(p14(x,1))

print counts    
print counts.index(max(counts))