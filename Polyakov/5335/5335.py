k=0
for x in range(int('10000',8),int('77777',8)+1):
    y=oct(x)[2:]
    if y.count('6')==1:
        pos=y.index('6')
        if pos==0:
            if int(y[1])%2==0:
                k+=1
        if pos==4:
            if int(y[3])%2==0:
                k+=1
        if 0<pos<4:
            if (int(y[pos-1])%2==0)and(int(y[pos+1])%2==0):
                k+=1
print(k)
