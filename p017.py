lib = ['','one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
libTens = ['','ten','twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']

def genString(n):
    string =''
    if n/1000:
        return 'onethousand'
    elif n/100:
        string += lib[n/100] + 'hundred'
        if (n/100 != 0) & (n%100 == 0):
            return string
        if (n%100 != 0):
            string += 'and'
    if (n%100 < 20) & (n%100 > 0):
        string += lib[n%100]
        return string
    if (n%100 > 19):
        string += libTens[(n%100)/10] +lib[(n%100%10)]
        return string      

TotLength = 0
LongString = ''
for x in range(1000):
    beta = genString(x+1)
    TotLength += len(beta)
    LongString += beta

print TotLength
# print LongString