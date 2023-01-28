MinR=1000000000000000000000000000000000000000000000000000000
for X in range(1,1000):
    x=oct(X)[3:]
    for Y in range(1,1000):
        y=oct(Y)[3:]
        R=int(('36'+(x)+'53'),8)-int(('4'+(y)+'3'),8)
        if R>0:
            MinR=min(MinR,R)
print(R)            
            
