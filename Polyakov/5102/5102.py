k=0
for n in range(1,100000):
    n2=bin(n)[2:]
    if n%2==0:
        n2='1'+n2+'11'
    else:
        n2='11'+n2+'0'
    R=int(n2,2)
    if (500<=R<=1000):
        k+=1
print(k)        
    
