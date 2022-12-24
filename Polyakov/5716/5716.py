k=0
for N in range(100000,1000000):
    x=N
    while x>0:
        pCifra=x%12
        x=x//12
    if N%pCifra==0:
        k+=1
print(k)        
